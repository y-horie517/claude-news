# 巡回する情報源

## 一次情報（必ず毎回確認する）

**WebFetch で実際に取れる URL を書いています。** 別のURLに変えないこと（GitHub の blob ページや docs.claude.com は中身が取れません）。

| 種別 | 取得に使う URL | 見るもの |
|---|---|---|
| Claude Code CHANGELOG | `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` | 前回チェック以降のバージョン差分。**速報の主軸**。記事中のリンクは `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md` を使ってよい |
| Claude Code ベストプラクティス | `https://code.claude.com/docs/en/best-practices` | 「型」と「TIPS」の一次ソース。質が高い |
| Claude Code ドキュメント | `https://code.claude.com/docs/en/overview` ／ 目次は `https://code.claude.com/docs/llms.txt` | 新しいページ・記述の変化 |
| Claude Platform リリースノート | `https://platform.claude.com/docs/en/release-notes/overview` | モデル・API・Console の変更 |
| 導入事例 | `https://claude.com/customers` | 企業の導入事例（チーム展開の題材） |

## 取れない URL（試さないこと）

- `https://www.anthropic.com/...` — **サンドボックスの egress でブロックされます**（`EGRESS_BLOCKED`）。公式ニュースは WebSearch の結果本文で拾うか、`claude.com` 側の同等ページを使う
- `https://github.com/**/blob/**` — HTML の外枠しか返りません。必ず `raw.githubusercontent.com` に読み替える
- `https://docs.claude.com/...` — `code.claude.com` / `platform.claude.com` に 301 されます。最初から新URLで取る

## 二次情報（事例集めに使う。仕様の根拠にはしない）

- WebSearch: `"Claude Code" tips` / `"Claude Code" workflow` （直近1週間に絞る）
- WebSearch 日本語: `Claude Code 使い方` / `Claude Code 事例` （Zenn / Qiita / はてなブログ）
- WebSearch: `site:reddit.com/r/ClaudeAI` の直近の話題
- Hacker News の Claude 関連スレッド

**WebSearch は egress 制限の外側で動くので必ず使えます。** 個別記事の WebFetch がブロックされたときは、検索結果の抜粋だけで書ける範囲にとどめ、`unverified` として明示すること。

## 前回チェック時点

朝刊エージェントは速報セクションを書いたあと、確認した CHANGELOG の最新バージョンをここに記録する。
次回はこのバージョンより新しいものだけを「速報」として扱う。

- last_changelog_version: v2.1.250
- last_checked_at: 2026-08-28
