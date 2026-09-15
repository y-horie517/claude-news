# Artifact テンプレートの使い方

`template/digest.html` を**必ず出発点**にしてください。CSS は触らず、`<div class="paper">` の中身だけを差し替えます。
デザインは固定です。毎回作り直すとブレるので、`artifact-design` スキルを読み込む必要はありません。

## 使えるクラス

| 用途 | 書き方 |
|---|---|
| 3行サマリー | `<div class="lede"><p>…</p>…</div>` |
| **節の要点**（各節の冒頭に置く） | `<ul class="keypoints"><li>…</li><li>…</li></ul>` |
| 節 | `<section class="sec">` ＋ `<div class="sec-rail"><span class="sec-no">01</span><span class="sec-tag">ラベル</span></div>` ＋ `<h2 class="sec-title">` ＋ `<div class="sec-body">` |
| 節の中の項目 | `<div class="item"><h3 class="item-h">…</h3><p>…</p></div>` |
| 番号つき項目 | `<h3 class="item-h"><span class="num">1</span>見出し</h3>` |
| 囲み | `<div class="card"><h3 class="card-h">見出し</h3>…</div>` |
| 課題・答え合わせの囲み | `<div class="card task">` |
| 図 | `<figure><div class="diagram"><pre class="mermaid">…</pre></div><figcaption>図1: 説明</figcaption></figure>` |
| コード | `<pre><code>…</code></pre>` |
| 表 | `<div class="table-wrap"><table>…</table></div>` |
| リスト | `<ul class="plain">` / `<ol class="plain">` |
| 出典 | `<p class="src"><a href="URL">タイトル</a></p>`（「出典」ラベルは自動で付く） |
| 未確認の情報 | `<p class="unverified">…</p>`（「未確認」ラベルが自動で付く） |
| **数値の並び** | `<div class="stats"><div class="stat"><b>54%</b><span>コメントが付いた PR</span></div>…</div>` |
| **失敗と正解の対比** | `<div class="vs"><div class="bad"><h4>…</h4>…</div><div class="good"><h4>…</h4>…</div></div>` |
| **用語ミニ表** | `<dl class="terms"><dt>サブエージェント</dt><dd>親とは別のコンテキストで動く子セッション</dd></dl>` |
| 強調 | `<mark>…</mark>` |

## 節番号（sec-no）と ラベル（sec-tag）

| sec-no | sec-tag | 中身 |
|---|---|---|
| 01 | ベストプラクティス | 看板。図1枚＋**コードブロック必須**＋アンチパターン |
| 02 | 深掘り連載 | `state/curriculum.md` の今日のテーマ。図1枚以上 |
| 03 | 開発TIPS | 3本 |
| 04 | 事例 | 1〜2本。うち1本はチーム／業務展開 |
| 05 | 速報 | 表（いつ / 何が / どう効くか） |
| 06 | コマンド早見 | **コマンドだけ**の2列表 |
| 07 | きょうの課題 | `card task` に課題、続けて `card task` に模範解答 |

## 地の文をどこへ逃がすか

**地の文が3段落、または400字を超えて続いたら、上の部品のどれかに割る。** これは `scripts/readability-check.py` が検査します。

| 中身 | 使う部品 | Markdown 側の書き方 |
|---|---|---|
| 節の要点（3行以内） | `<ul class="keypoints">` | `>` の引用の箇条書き |
| 数値が3つ以上絡む話 | `<div class="stats">` | 2列の表（値 / 何の数字か） |
| アンチパターンと正解 | `<div class="vs">` | `#### ❌ …` / `#### ✅ …` の小見出し2つ |
| 用語の定義 | `<dl class="terms">` | 2列の表（用語 / 意味） |
| A と B の違い・設定値 | `<div class="table-wrap">` | 表 |
| 構造・フロー・関係 | `<pre class="mermaid">` | ```mermaid フェンス |

- `stats` は 04 事例の実績値に使う。数字を地の文に埋めないこと。
- `vs` は 01 のアンチパターンに使う。**失敗する側のコードも短く並べる**。
- `terms` は節末に置く。本文の括弧に「（〜とは…）」と書かない。

## 注意

- コードは `<pre><code>` に入れる。**01 の節ではコードブロックを省かない**（この節の存在理由がコードと図です）。
- Mermaid のラベルは必ず `["…"]` とダブルクォートで囲む。`()` `:` `,` が裸で入ると描画に失敗します。
- 図は `<pre class="mermaid">` の中に**インデントなし**で書く（先頭の空白でパースが崩れることがある）。
- 題字の日付・号数・読了目安（`.masthead-meta`）を毎回更新すること。読了目安は 10〜12分。
- HTML の先頭は `<title>Claude Daily</title>` のまま変えない（タブとギャラリーでの名前が毎回変わると別物に見えるため）。
