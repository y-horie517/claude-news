# 巡回する情報源

## 一次情報（必ず毎回確認する）

**WebFetch で実際に取れる URL を書いています。** 別のURLに変えないこと（GitHub の blob ページや docs.claude.com は中身が取れません）。

| 種別 | 取得に使う URL | 見るもの |
|---|---|---|
| Claude Code CHANGELOG | `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` | 前回チェック以降のバージョン差分。**速報の主軸**。記事中のリンクは `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` を使ってよい |
| Claude Code ベストプラクティス | `https://code.claude.com/docs/en/best-practices` | **「① ベストプラクティス」節の一次ソース。**「型」と「TIPS」もここから |
| Claude Code ドキュメント | `https://code.claude.com/docs/en/overview` ／ 目次は `https://code.claude.com/docs/llms.txt` | 新しいページ・記述の変化 |
| Claude Platform リリースノート | `https://platform.claude.com/docs/en/release-notes/overview` | モデル・API・Console の変更 |
| 導入事例 | `https://claude.com/customers` | 企業の導入事例（チーム展開の題材） |
| Anthropic ニュース | `https://www.anthropic.com/news` | 製品・モデルの発表 |
| Anthropic Engineering | `https://www.anthropic.com/engineering` | 使い方の設計論。**深掘り連載の一次ソースとして質が高い** |

## URL の書き方の注意

ネットワークは **Full**（全ドメイン許可）です。egress でブロックされることはありません。ただし URL の形によっては中身が取れません。

- `https://github.com/**/blob/**` — HTML の外枠しか返りません。必ず `raw.githubusercontent.com/<org>/<repo>/<branch>/<path>` に読み替える
- `https://docs.claude.com/...` — `code.claude.com/docs/...`（Claude Code）/ `platform.claude.com/docs/...`（API・Console）に 301 されます。最初から新URLで取る
- `https://www.anthropic.com/news` `https://www.anthropic.com/engineering` — 読めます（公式ニュース・技術記事の一次情報）

## 二次情報（事例集めに使う。仕様の根拠にはしない）

- WebSearch: `"Claude Code" tips` / `"Claude Code" workflow` （直近1週間に絞る）
- WebSearch 日本語: `Claude Code 使い方` / `Claude Code 事例` （Zenn / Qiita / はてなブログ）
- WebSearch: `site:reddit.com/r/ClaudeAI` の直近の話題
- Hacker News の Claude 関連スレッド

個別記事は WebFetch で**本文まで読んでから**書くこと。検索結果の抜粋だけで書いた場合は `unverified` として明示する。

## 前回チェック時点

エージェントは速報セクションを書いたあと、確認した CHANGELOG の最新バージョンをここに記録する。
次回はこのバージョンより新しいものだけを「速報」として扱う。

- last_changelog_version: v2.1.258
- last_checked_at: 2026-09-02（第012号。CHANGELOG に v2.1.258 より新しい版なし）
