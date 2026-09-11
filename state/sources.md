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

- last_changelog_version: v2.1.269
- last_checked_at: 2026-09-12（第021号。CHANGELOG に v2.1.269 が追加された。項目数が非常に多い回で、`claude plugin eval`（プラグインのeval実行・JSON/HTMLレポート）、`/output-style [name]` の追加、`bashEditDiffEnabled`、`OTEL_METRICS_INCLUDE_REPOSITORY`、`CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS`、`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`(1-256)、`/focus` のスピナーTIP、`!` 始まりの deny/ask ルールが書いたソース外に及んでいた不具合の修正（裸の `!` は無視）、コンパクション後の git status を現在値に修正、プロンプトキャッシュ破壊2件の修正、クラウドの定期実行（routine）の二重起動とサブエージェント使用時の早期完了扱いの修正、`/ultrareview --post` が直接PRにコメントする変更などを速報で扱った。Platform リリースノートは 9/10 の Managed Agents `auto` と `ant beta:sessions connect` のままで新規なし、anthropic.com/news も 9/10 の「Detecting and countering misuse of AI」のまま、anthropic.com/engineering は 4/23 から更新なし。claude.com/customers は 9/4 の Carvana が最新で、未報告だった 9/3 の Qonto を④の一次情報として使った。②の連載はカリキュラム15番の Artifacts で、`code.claude.com/docs/en/artifacts` を一次情報にした。①は新設の `code.claude.com/docs/en/plugin-evals` が一次情報。なお docs の Output styles ページには「`/output-style` は v2.1.91 で削除」の注記が残っており、CHANGELOG と食い違っている）
- 前回: 2026-09-11（第020号。CHANGELOG に v2.1.268 が追加された。項目が非常に多く、`/plugin` メニューを閉じた時点でインストール・有効化・無効化が反映されるようになった変更、`claude plugin install/uninstall/update/enable/disable` への `--json` 追加と `list --json` の `errorDetails`/`noteDetails`、WebFetch の300秒デッドライン（`CLAUDE_CODE_WEBFETCH_DEADLINE_MS`）、`ANTHROPIC_BASE_URL` 経由で全ターンが HTTP 400 になっていた v2.1.265 以降の回帰修正、シンボリックリンクディレクトリと `env -C`/`eval` 同一行での deny すり抜け修正、git URL のトークンと `${VAR}` 由来シークレットの表示修正、`CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` の不発修正、ゲートウェイ関連の `gatewayInternalNetworks` などを速報で扱った。Platform リリースノートは 9/10 に更新があり、Managed Agents の権限ポリシー `auto`（`evaluation` フィールド）と `ant beta:sessions connect`（`--web`）を扱った。anthropic.com/news も 9/10 に「Detecting and countering misuse of AI: September 2026」が追加され1行で触れた。anthropic.com/engineering は 4/23 から更新なし。claude.com/customers は 9/4 の Carvana が最新で既報のため、④は二次情報2本（Yappli Tech Blog / Qiita）で構成した）
- 前回: 2026-09-10（第019号。CHANGELOG に v2.1.266 と v2.1.267 が追加された。v2.1.266 は `CLAUDE_CODE_USE_GATEWAY` が単独で Cloud ゲートウェイのサインインを強制していた v2.1.265 の回帰修正1件のみ。v2.1.267 は項目が非常に多く、`maxEffortLevel` の追加、`--system-prompt-snapshot off` の追加、MCP／コネクタ／`/model` 切替／セッション再開に起因するプロンプトキャッシュ破壊の修正が10件以上、マーケットプレイスのバックスラッシュによる containment 検査回避の修正、5MB 超セッション再開で並列ツール呼び出しとフック出力が落ちる不具合の修正などを速報で扱った。Platform リリースノートは 9/3 の ant CLI v1.30.0 と Google Cloud のper-message effort ベータのまま、anthropic.com/news は 9/1 の Fable 5.1 / Mythos 5.1 のまま、anthropic.com/engineering も 4/23 から更新なし。claude.com/customers は 9/4 の Carvana が最新で既報）
- 前回: 2026-09-09（第018号。CHANGELOG に v2.1.265 が追加された。項目は多数で、`--plugin-dir` のフォルダ指定と動的読み込み、プロンプトキャッシュ再利用の破壊修正3件、`--worktree` 起動の並列チェックアウト高速化、`/model opus[1m]` の拒否修正、ツール結果のディスク保存1GB上限、プラグインパスのバックスラッシュによるシンボリックリンク検査回避の修正などを速報で扱った。v2.1.264 は CHANGELOG に項目なし。Platform リリースノートは 9/3 の ant CLI v1.30.0 のまま、anthropic.com/news は 9/1 の Fable 5.1 / Mythos 5.1 のまま、anthropic.com/engineering も 4/23 から更新なし）
- 前回: 2026-09-08（第017号。CHANGELOG は v2.1.263 のままで新規バージョンなし。Platform リリースノートは 9/3 の ant CLI v1.30.0 が最新、anthropic.com/news は 9/1 の Fable 5.1 / Mythos 5.1 が最新、anthropic.com/engineering も 4/23 から更新なし。いずれも既報のため速報は「該当なし」で執筆）
- 前回: 2026-09-07（第016号。CHANGELOG は v2.1.263 のみ新規で、中身は「Bug fixes and reliability improvements」の1行のみ。v2.1.262 は CHANGELOG に項目がない。Platform リリースノートは 9/3 の ant CLI v1.30.0 から更新なし。anthropic.com/news は 9/1 の Fable 5.1 / Mythos 5.1 から新規なし。anthropic.com/engineering も 4/23 が最新で新規なし）
