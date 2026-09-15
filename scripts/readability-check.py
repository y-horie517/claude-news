#!/usr/bin/env python3
"""Claude Daily の原稿が「読みやすさの規約」を守っているか機械的に検査する。

    python3 scripts/readability-check.py digest/2026/09/2026-09-02.md
    python3 scripts/readability-check.py --summary digest/2026/09/*.md

規約の本体は prompts/style-guide.md の「読みやすさの規約」。閾値を変えるときは
両方を同時に直すこと。標準ライブラリだけで動き、ネットワークは使わない。
"""

import argparse
import re
import sys

# ── 閾値（prompts/style-guide.md と同じ値にすること）──────────────────
MAX_SENTENCE = 80          # 1文の字数
MAX_PARA_CHARS = 200       # 1段落の字数
MAX_PARA_SENTENCES = 3     # 1段落の文数
MAX_RUN_PARAS = 3          # 図表を挟まずに続けてよい段落の数
MAX_RUN_CHARS = 400        # 同上、字数
MAX_BOLD_PER_SEC = 5       # 1節の太字の箇所
MIN_DIAGRAMS = 3           # 1号の図の枚数
MIN_TABLES = 4             # 1号の表の数
TOTAL_BUDGET = 4500        # 1号の地の文の字数

# 節ごとの地の文の上限。キーは節見出しに含まれる丸数字（3行サマリーだけ "lede"）
SECTION_BUDGET = {
    "lede": 180,
    "①": 1000,
    "②": 1200,
    "③": 450,
    "④": 600,
    "⑤": 200,
    "⑥": 0,
    "⑦": 760,   # 課題700 ＋ 末尾の「あすの予告」60（⑦ の節に含まれる）
}

# 直訳調・冗長表現。左辺に当たったら言い換える
CLICHES = [
    (r"することができ(ます|る)", "「〜できます」に直す"),
    (r"することが可能(です|だ)", "「〜できます」に直す"),
    (r"を行(う|います|った|い)", "動詞そのもので書く（実行する・作る）"),
    (r"を実施(する|します)", "動詞そのもので書く"),
    (r"これにより", "主語を立てて書く"),
    (r"それによって|それにより", "主語を立てて書く"),
    (r"という点において", "「〜は」「〜では」に直す"),
    (r"に関して(は)?", "「〜は」「〜では」に直す"),
    (r"の場合においては", "「〜のときは」に直す"),
]

FENCE = re.compile(r"^\s*```")
HEADING = re.compile(r"^#{1,6}\s")
TABLE_ROW = re.compile(r"^\s*\|")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]\s|\d+[.)]\s)")
QUOTE = re.compile(r"^\s*>")
CAPTION = re.compile(r"^\s*図\s*\d+\s*[:：]")
SOURCE = re.compile(r"^\s*(?:[-*+]\s+)?出典\s*[:：]")
HRULE = re.compile(r"^\s*(?:-{3,}|─+.*─+)\s*$")
HTML_TAG = re.compile(r"<div|<p class|<h3|</content|<span class|<section")
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
INLINE_CODE = re.compile(r"`[^`]*`")
CIRCLED = re.compile(r"[①②③④⑤⑥⑦⑧⑨]")
# 段落の頭に置く「**前提**:」のようなラベル。見出しの代わりなので太字には数えない
BOLD_LABEL = re.compile(r"^\s*\*\*[^*]+\*\*\s*[:：]?")


def clean(text):
    """字数・文長を数えるための正規化。コード・リンクURL・記法は数えない。"""
    text = INLINE_CODE.sub("", text)
    text = LINK.sub(r"\1", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\*\*|__|\*|~~", "", text)
    text = LIST_ITEM.sub("", text)
    text = re.sub(r"^\s*>\s*", "", text)
    return text.strip()


def count(text):
    return len(re.sub(r"\s", "", text))


def sentences(text):
    parts = re.split(r"(?<=[。！？])", text)
    return [p.strip() for p in parts if p.strip()]


class Block:
    """1行〜数行のまとまり。kind で見た目の種類を持つ。"""

    def __init__(self, kind, line, text=""):
        self.kind = kind      # prose / list / quote / table / code / mermaid / heading / source / caption / rule
        self.line = line      # 1始まりの行番号
        self.text = text


def parse(path):
    """Markdown を節ごとのブロック列に分解する。コードフェンスの中は解釈しない。"""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    sections = []                       # [(key, title, line, [Block, ...])]
    current = ("lede", "（題字と3行サマリー）", 1, [])
    sections.append(current)

    in_fence = False
    fence_kind = None
    fence_line = 0
    para_lines = []
    para_line = 0

    def flush_para():
        nonlocal para_lines, para_line
        if para_lines:
            current[3].append(Block("prose", para_line, " ".join(para_lines)))
            para_lines = []

    for no, raw in enumerate(lines, start=1):
        line = raw.rstrip()

        if FENCE.match(line):
            if in_fence:
                current[3].append(Block(fence_kind, fence_line))
                in_fence = False
                fence_kind = None
            else:
                flush_para()
                in_fence = True
                fence_line = no
                fence_kind = "mermaid" if "mermaid" in line.lower() else "code"
            continue
        if in_fence:
            continue

        if not line.strip():
            flush_para()
            continue

        if HEADING.match(line):
            flush_para()
            if line.startswith("## "):
                title = line[3:].strip()
                hit = CIRCLED.search(title)
                key = hit.group(0) if hit else ("lede" if "3行" in title else title)
                current = (key, title, no, [])
                sections.append(current)
            else:
                current[3].append(Block("heading", no, line))
            continue

        if TABLE_ROW.match(line):
            flush_para()
            if not (current[3] and current[3][-1].kind == "table"):
                current[3].append(Block("table", no))
            continue

        if SOURCE.match(line):
            flush_para()
            current[3].append(Block("source", no, line))
            continue

        if CAPTION.match(line):
            flush_para()
            current[3].append(Block("caption", no, line))
            continue

        if HRULE.match(line):
            flush_para()
            current[3].append(Block("rule", no, line))
            continue

        if LIST_ITEM.match(line):
            flush_para()
            current[3].append(Block("list", no, line))
            continue

        if QUOTE.match(line):
            flush_para()
            current[3].append(Block("quote", no, line))
            continue

        if not para_lines:
            para_line = no
        para_lines.append(line.strip())

    flush_para()
    return lines, [s for s in sections if s[3] or s[0] != "lede"]


# ── 個別の検査 ─────────────────────────────────────────────────────
def check(path):
    lines, sections = parse(path)
    ng = []

    def add(line, name, reason, quote=""):
        tail = f"  — {quote[:40]}" if quote else ""
        ng.append((line, name, f"NG {path}:{line} [{name}] {reason}{tail}"))

    # 1. HTML タグ混入（コードフェンスの外だけを見る）
    in_fence = False
    for no, raw in enumerate(lines, start=1):
        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        hit = HTML_TAG.search(raw)
        if hit:
            add(no, "htmlタグ", f"Markdown に HTML タグ `{hit.group(0)}` が入っている", raw.strip())

    total_chars = 0
    diagrams = 0
    tables = 0
    sec_diagrams = {}
    sec_code = {}

    for key, title, line, blocks in sections:
        sec_chars = 0
        bold = 0
        run_paras, run_chars, run_line = 0, 0, 0
        sec_diagrams[key] = 0
        sec_code[key] = 0

        for block in blocks:
            if block.kind == "mermaid":
                diagrams += 1
                sec_diagrams[key] += 1
            elif block.kind == "code":
                sec_code[key] += 1
            elif block.kind == "table":
                tables += 1

            if block.kind in ("prose", "list", "quote", "heading"):
                bold += block.text.count("**") // 2
                if BOLD_LABEL.match(block.text):
                    bold -= 1                   # 段落頭のラベルは強調ではない
                text = clean(block.text)
                if block.kind != "heading":     # 見出しは構造。地の文には数えない
                    sec_chars += count(text)

                # 4. 文長
                for sent in sentences(text):
                    if count(sent) > MAX_SENTENCE:
                        add(block.line, "文が長い",
                            f"1文 {count(sent)}字（上限 {MAX_SENTENCE}字）。1文1主張に分ける",
                            block.text)

            # 5. 段落長 / 6. 地の文の連続
            if block.kind == "prose":
                text = clean(block.text)
                chars, sents = count(text), len(sentences(text))
                if chars > MAX_PARA_CHARS:
                    add(block.line, "段落が長い",
                        f"1段落 {chars}字（上限 {MAX_PARA_CHARS}字）。表・図・箇条書きに割る",
                        block.text)
                elif sents > MAX_PARA_SENTENCES:
                    add(block.line, "段落が長い",
                        f"1段落 {sents}文（上限 {MAX_PARA_SENTENCES}文）。段落を分ける",
                        block.text)
                if run_paras == 0:
                    run_line = block.line
                run_paras += 1
                run_chars += chars
            elif block.kind in ("table", "mermaid", "code", "list", "quote"):
                if run_paras > MAX_RUN_PARAS or run_chars > MAX_RUN_CHARS:
                    add(run_line, "地の文が続く",
                        f"図表を挟まず地の文が {run_paras}段落 {run_chars}字 続く。表・図・箇条書きに割る")
                run_paras, run_chars = 0, 0

            # 12. 出典行
            if block.kind == "source" and len(LINK.findall(block.text)) > 1:
                add(block.line, "出典が1行に複数",
                    f"出典 {len(LINK.findall(block.text))}件が1行にある。1行1件の箇条書きにする")

            # 11. 直訳調
            if block.kind in ("prose", "list", "quote", "heading", "caption"):
                for pattern, fix in CLICHES:
                    for hit in re.finditer(pattern, clean(block.text)):
                        add(block.line, "直訳調", f"「{hit.group(0)}」は{fix}", block.text)

        if run_paras > MAX_RUN_PARAS or run_chars > MAX_RUN_CHARS:
            add(run_line, "地の文が続く",
                f"図表を挟まず地の文が {run_paras}段落 {run_chars}字 続く。表・図・箇条書きに割る")

        total_chars += sec_chars

        # 2. 節ごとの字数
        budget = SECTION_BUDGET.get(key)
        if budget is not None and sec_chars > budget:
            add(line, "節が長い",
                f"「{title[:24]}」の地の文が {sec_chars}字（上限 {budget}字）")

        # 10. 太字密度
        if bold > MAX_BOLD_PER_SEC:
            add(line, "太字が多い",
                f"「{title[:24]}」に太字 {bold}箇所（上限 {MAX_BOLD_PER_SEC}箇所）。強調が信号でなくなる")

    # 3. 全体の字数
    if total_chars > TOTAL_BUDGET:
        add(1, "全体が長い", f"地の文 {total_chars}字（上限 {TOTAL_BUDGET}字）")

    # 7. 図の枚数
    if diagrams < MIN_DIAGRAMS:
        add(1, "図が足りない", f"mermaid {diagrams}枚（最低 {MIN_DIAGRAMS}枚）")
    for key in ("①", "②"):
        if key in sec_diagrams and sec_diagrams[key] == 0:
            add(1, "図が足りない", f"{key} の節に図がない")

    # 8. 表の数
    if tables < MIN_TABLES:
        add(1, "表が足りない", f"表 {tables}個（最低 {MIN_TABLES}個）")

    # 9. ① のコード
    if "①" in sec_code and sec_code["①"] == 0:
        add(1, "コードがない", "① ベストプラクティスに実行可能なコード／設定がない")

    metrics = {
        "chars": total_chars,
        "diagrams": diagrams,
        "tables": tables,
        "sections": {k: v for k, v, in [(s[0], s[1]) for s in sections]},
    }
    return sorted(ng), metrics, sections


def summarize(path, sections):
    """--summary 用。違反ではなく指標だけを出す。"""
    chars = long_sents = long_paras = 0
    longest = 0
    for _, _, _, blocks in sections:
        for block in blocks:
            if block.kind in ("prose", "list", "quote", "heading"):
                text = clean(block.text)
                if block.kind != "heading":
                    chars += count(text)
                for sent in sentences(text):
                    n = count(sent)
                    longest = max(longest, n)
                    if n > 90:
                        long_sents += 1
            if block.kind == "prose" and count(clean(block.text)) > 200:
                long_paras += 1
    return chars, long_paras, long_sents, longest


def main():
    parser = argparse.ArgumentParser(description="Claude Daily の原稿の読みやすさを検査する")
    parser.add_argument("files", nargs="+", help="検査する Markdown のパス")
    parser.add_argument("--summary", action="store_true", help="違反を出さず指標だけを出す")
    args = parser.parse_args()

    failed = False
    for path in args.files:
        try:
            ng, metrics, sections = check(path)
        except OSError as err:              # 読めないときは素通しする（fail open）
            print(f"SKIP {path}: {err}", file=sys.stderr)
            continue

        if args.summary:
            chars, paras, sents, longest = summarize(path, sections)
            print(f"{path}\t地の文={chars}\t図={metrics['diagrams']}\t表={metrics['tables']}"
                  f"\t200字超の段落={paras}\t90字超の文={sents}\t最長文={longest}\t違反={len(ng)}")
            continue

        for _, _, message in ng:
            print(message)
        if ng:
            failed = True
            counts = {}
            for _, name, _ in ng:
                counts[name] = counts.get(name, 0) + 1
            breakdown = " / ".join(f"{k} {v}件" for k, v in sorted(counts.items(), key=lambda x: -x[1]))
            print(f"\n{path}: NG {len(ng)}件 — {breakdown}")
            print(f"  地の文 {metrics['chars']}字 / 図 {metrics['diagrams']}枚 / 表 {metrics['tables']}個")
        else:
            print(f"OK {path} — 地の文 {metrics['chars']}字 / 図 {metrics['diagrams']}枚 / 表 {metrics['tables']}個")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
