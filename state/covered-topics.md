# 既出トピック台帳

**重複を防ぐための台帳です。** 執筆前に必ず読み、ここに載っているトピックは繰り返さないこと。
触れる必要があるときは「詳しくは 2026-08-29 の号 を参照」のようにリンクするだけにする。

記入フォーマット: `- YYYY-MM-DD [カテゴリ] トピック名 — 一行要約`
カテゴリ: `BP`(ベストプラクティス) / `連載` / `TIPS` / `事例` / `速報` / `課題`

> 2026-09-02 以前の行にある `朝` / `夕` と `型` は、朝刊・夕刊の2号立てだった頃の表記です。
> 既存の行はそのまま残し、新しい行だけ上のフォーマットで書いてください。

## 2026-08

- 2026-08-28 朝 [型] 検証つきで任せる — チェック(テスト/ビルド)とサブエージェントの二段レビューで任せきりの精度を上げる
- 2026-08-28 朝 [TIPS] CLAUDE.mdは索引として保つ — 詳細はskillに切り出し、CLAUDE.mdを短く保つ
- 2026-08-28 朝 [TIPS] 訂正は2回まで。3回目は/clear — 失敗した試行錯誤の蓄積を避ける
- 2026-08-28 朝 [TIPS] 調査はサブエージェントに逃がす — メインコンテキストを汚さず調査結果だけ受け取る
- 2026-08-28 朝 [事例] Stripe 署名済みバイナリで1,370名に配布 — Scala→Java 1万行移行を10週間相当から4日に短縮
- 2026-08-28 朝 [事例] 30名規模組織のフェーズドロールアウト — 1クオーターでスキル22個・フック11個を整備、35%生産性向上
- 2026-08-28 朝 [速報] v2.1.248 --restrictedフラグ・experimental.cacheTtl・/doctor診断
- 2026-08-28 朝 [速報] v2.1.247 SendFeedbackツール・/claude-api cost-optimize強化
- 2026-08-28 朝 [課題] 検証つきワークフローを体験する — 失敗するテスト→実装→サブエージェントレビューの一連を試す
- 2026-08-28 夕 [連載] 第1回 コンテキストという概念 — 起動時に約7,850トークン、コンパクションで何が残り何が消えるか
- 2026-08-28 夕 [TIPS] /context・/context all で実測する — 読み込まれたCLAUDE.mdの確認が一次診断
- 2026-08-28 夕 [TIPS] /btw は会話履歴に残さず質問できる — 本筋を汚さない小さな確認用
- 2026-08-28 夕 [TIPS] /autocompact で自動コンパクションの閾値を設定
- 2026-08-28 夕 [TIPS] フックのコンテキストコストはゼロ — ログ絞り込みなど「読ませずに済ませる」が最強
- 2026-08-28 夕 [型] 縛りの4段階 — プロンプト内依頼 / `/goal` 条件 / Stopフック / `/code-review`
- 2026-08-28 夕 [事例] モノレポでコンテキストをチームの予算として設計 — ディレクトリ別CLAUDE.md、claudeMdExcludes、permissions.denyのRead、worktree.sparsePaths
- 2026-08-28 夕 [事例] OTEL_LOG_TOOL_DETAILS=1 と skill_activated で未使用Skillを実測 — 統廃合をログで判断する
- 2026-08-28 夕 [事例] 設定監査によるオーバーヘッド削減の報告（61%減・44%減、いずれも未確認）
- 2026-08-28 夕 [用語] コンパクション / 1Mコンテキスト対応モデル / CLAUDE.md 200行・4MiB / MEMORY.md 200行・25KB
- 2026-08-29 朝 [型] 探索→計画→実装→コミット（Plan Mode） — Shift+Tab/--permission-mode planで探索・計画を実装から分離、Ctrl+Gで計画をエディタ編集
- 2026-08-29 朝 [TIPS] 使うCLIツールを教えて使わせる — gh/aws/gcloud/sentry-cli、未知のCLIも--helpから学習させられる
- 2026-08-29 朝 [TIPS] 許可リストとサンドボックスでプロンプトを減らす — /permissionsで安全なコマンドを許可登録、/sandboxでOSレベル隔離
- 2026-08-29 朝 [TIPS] フックで「毎回必ず」を保証する — CLAUDE.mdは助言的、フック（.claude/settings.json）は決定的に実行
- 2026-08-29 朝 [事例] Spellbook 契約レビューAI — Fable計画→Sonnet実行→Fableレビューの体制、契約完了10時間→約1時間、月53万件処理
- 2026-08-29 朝 [事例] EvenUp 人身傷害の書類作成支援 — 従業員200名超にClaude Enterprise/Code展開、文書作成8〜15時間→約30分（99%減）
- 2026-08-29 朝 [事例] Rocket Money 家計管理アプリ — AI金融エージェント「Rowan」開発、月間コミット数11倍（11件→128件）
- 2026-08-29 朝 [課題] Plan Modeで探索→計画→実装を体験する — Next.jsの小機能追加でCtrl+Gの計画編集を試す
- 2026-08-29 夕 [連載] 第2回 CLAUDE.md の書き方 — 読み込み階層と順序、インポートの限界、paths つきルール、効くもの/効かないもの
- 2026-08-29 夕 [型] 指示の置き場所を決める判断フロー — 毎回必要か/パス限定か/必ず実行か で CLAUDE.md・rules・Skill・フックを選ぶ
- 2026-08-29 夕 [TIPS] CLAUDE.mdはシステムプロンプトではなくユーザーメッセージとして渡される — だから厳密な遵守は保証されない
- 2026-08-29 夕 [TIPS] @path インポートではコンテキストは減らない — 起動時に展開されて載る。減らすのは paths つきルールと Skill
- 2026-08-29 夕 [TIPS] ブロックレベルHTMLコメントは注入前に除去される — トークンを使わず人間向けメモを残せる
- 2026-08-29 夕 [TIPS] IMPORTANT は守られない1行にだけ付ける — 多用すると効かなくなる
- 2026-08-29 夕 [TIPS] 「この行を消したら Claude はミスをするか」で剪定する — /doctor が削減案を出す（v2.1.206以降）
- 2026-08-29 夕 [TIPS] AGENTS.md は読まれない — @AGENTS.md インポートかシンボリックリンクで橋渡し（Windowsはインポート推奨）
- 2026-08-29 夕 [事例] ZOZO のレビュー指摘→.claude/rules 自動反映 — Routinesで毎週月曜9時、必要な時だけPR、根拠URLを紐づけ（効果の数値なし）
- 2026-08-29 夕 [用語] 管理ポリシー/ユーザー/プロジェクト/ローカルの4スコープ / paths フロントマター / InstructionsLoaded フック / CLAUDE.md 200行・4MiB
- 2026-08-30 朝 [型] ファンアウト移行 — 対象ファイル一覧を作りclaude -pのループや/batchで1ファイル=1セッションに並列処理する
- 2026-08-30 朝 [TIPS] auto modeの分類器に安全な自動運転を任せる — スコープ逸脱等の危険な操作だけ止め、それ以外は確認なしで進む
- 2026-08-30 朝 [TIPS] Writer/Reviewerパターン — 実装セッションとは別の新鮮なコンテキストのセッションにレビューさせバイアスを避ける
- 2026-08-30 朝 [TIPS] PostModelSwitchフックでモデル切替を記録・PreModelSwitchでブロック — v2.1.251の新フック、from_model/to_modelを受け取る
- 2026-08-30 朝 [事例] Deepgram 音声認識API — 「書いて→検証させる」ループで非利用者比4〜10倍堅牢なコード、最生産性チームは実行コードの約95%がClaude生成
- 2026-08-30 朝 [事例] Classmethod 日本のクラウドインテグレーター — Rails/Next.js/Terraformに統合、開発時間最大90%減・レビュー80%減、月間PR数108件→165件
- 2026-08-30 朝 [速報] v2.1.251 PreModelSwitch/PostModelSwitchフック・サブエージェントのライブストリーミング・/costのキャッシュ行・パストラバーサル脆弱性修正
- 2026-08-30 朝 [課題] ファンアウト移行を小さく体験する — 相対importのエイリアス統一をclaude -pループで試す
- 2026-08-30 夕 [連載] 第3回 計画 → 実装 のループ — プランモードの入り方3種・承認3択・計画の受け渡し・検証で閉じるまで
- 2026-08-30 夕 [TIPS] `/plan` 接頭辞はその1プロンプトだけプランモードにする — モードを切り替えて戻す手間が要らない
- 2026-08-30 夕 [TIPS] プランモードは安全境界ではない — bypass permissions が使えるセッションではブロックが強制されない
- 2026-08-30 夕 [TIPS] useAutoModeDuringPlan（既定オン）— 計画中のシェルコマンドは分類器が審査し、確認は出ない
- 2026-08-30 夕 [TIPS] showClearContextOnPlanAccept — 承認と同時に探索フェーズのコンテキストを捨て、実装を空に近い状態で始める
- 2026-08-30 夕 [TIPS] 承認の3択は実装フェーズの権限モードの選択 — auto / 手動承認 / 計画続行。Shift+Tabで抜けると計画は未承認
- 2026-08-30 夕 [TIPS] 計画を承認するとセッションに計画由来のタイトルが自動生成される
- 2026-08-30 夕 [TIPS] AskUserQuestion で取材させ SPEC.md を書かせ、新セッションで実行する — 自己完結した仕様の条件
- 2026-08-30 夕 [TIPS] `for` ループは逐次。ファンアウトを本当に並列にするのは `xargs -P` — `for file in $(cat ...)` は空白で壊れる
- 2026-08-30 夕 [型] 検証(動くか)と計画との突き合わせ(頼んだものか)は別物 — 後者はサブエージェントに差分とPLAN.mdを渡す
- 2026-08-30 夕 [事例] AI-Native SDLC playbook（Anthropic）— intent.md→spec.md→plan.md→差分→レビュー所見の成果物連鎖、plan.mdをコミットしREVIEW.mdでレビュー観点を明文化、Claudeは所見のみで承認不可
- 2026-08-30 夕 [用語] permissions.defaultMode: "plan" / claudeCode.initialPermissionMode / /goal の3評決（未達・達成・不可能）・条件4,000文字
- 2026-08-31 朝 [型] 初見のリポジトリを3層防御で開く — 環境層(sandbox)/モデル層(auto mode分類器)/外部コンテンツ層の3層。設定ファイルは開く前にレビューする
- 2026-08-31 朝 [TIPS] Stop hookは8回連続ブロックで強制的に上書きされる — 検証ゲートを過信しない
- 2026-08-31 朝 [TIPS] /rewindのSummarize from here / up to hereで会話の一部だけを圧縮する
- 2026-08-31 朝 [TIPS] sandbox-runtime（anthropic-experimental）はOSSで監査できる — 84%のプロンプト削減を実現した設計
- 2026-08-31 朝 [事例] Vega サイバーセキュリティ — Opus/Sonnet/Haikuを階層的に使い分け、調査速度44倍・データコスト82%減・分析チーム時間67%回復
- 2026-08-31 朝 [事例] League ヘルスケア — 独自オーケストレーションツールSwarm、契約から全社展開まで実質1営業日、開発サイクル半減
- 2026-08-31 朝 [事例] Microsoft社内ロールアウトの学術研究（arXiv:2607.01418）— マージPR約24%増だが配布のみでは効果なし、継続利用が鍵
- 2026-08-31 朝 [速報] Inference hooksがClaude Enterpriseでベータ開始（2026-08-05）— chat/Cowork/Claude Code共通、プロンプトをallow/deny判定してから推論
- 2026-08-31 朝 [課題] Stop hookで検証を強制する — lintが通るまで終了しないhookを書かせ、ブロックと自己修正のループを観察する
- 2026-08-31 夕 [連載] 第4回 権限モードと安全性 — 6モードの比較・判定順序・auto mode分類器・保護パス/重要パス・隔離とのセット
- 2026-08-31 夕 [TIPS] Stop hookは終了コード2だけがブロック — 1は非ブロックのエラーでターンは終わる。`npm run lint || exit 2` で変換する
- 2026-08-31 夕 [TIPS] `stop_hook_active` はhook起因で継続中に true — 解決しない条件でブロックし続けないための入力
- 2026-08-31 夕 [TIPS] `hookSpecificOutput.additionalContext` はエラーでなく助言として継続させる — ループ保護は block と同じ
- 2026-08-31 夕 [TIPS] `"auto"` は .claude/settings.json / settings.local.json からは効かない — その場合ユーザー設定のdefaultModeも無視され組み込み既定になる
- 2026-08-31 夕 [TIPS] ルールの評価順は deny → ask → allow、最初の一致が勝つ — 具体性は順序を変えず、denyに例外は持たせられない
- 2026-08-31 夕 [TIPS] auto modeに入ると広いallowルールが一時的に落ちる — Bash(*)・Bash(python*)・パッケージマネージャのrun・Agent/Monitor。抜けると復元
- 2026-08-31 夕 [TIPS] 会話で述べた境界はブロック信号になるがコンパクションで消える — 確実にしたいならdenyルール
- 2026-08-31 夕 [TIPS] 保護パスは permissions.allow で開けられない — 検査がallow評価より前に走る（Edit(.claude/**) は無効）
- 2026-08-31 夕 [型] 「最悪の挙動で何が壊れうるか」を決めてからモードを選ぶ — 隔離を先に用意する
- 2026-08-31 夕 [事例] 権限ポリシーを配る（managed settings）— allowManagedPermissionRulesOnly で開発者のルールと --allowedTools を無視、/status と claude doctor で着弾確認、管理設定はフェイルクローズ
- 2026-08-31 夕 [事例] 50名以上向けロールアウトの4段階（パイロット→部門→複数部門→全社）という報告（systemprompt.io、二次情報）
- 2026-08-31 夕 [用語] 6つの権限モード / 保護パス(protected path) / 重要パス(critical path) / 分類器の停止条件(3連続・通算20回) / 分類器の実測値(偽陽性0.4%・見逃し17%/5.7%・プロンプト承認率93%) / disableAutoMode / disableBypassPermissionsMode / allowManagedPermissionRulesOnly

## 2026-09

- 2026-09-01 朝 [型] `/batch`でファンアウト移行を任せる — gitリポジトリ内で5〜30体のサブエージェントに自動分割、各自worktreeで作業しPRを作成
- 2026-09-01 朝 [TIPS] `/statusline`でコンテキスト残量を常時可視化する — 自然言語指示でスクリプトを`~/.claude/`に生成、設定も自動
- 2026-09-01 朝 [TIPS] `claude agents`（Agent view）で複数バックグラウンドセッションを1画面から見る — 状態別一覧とPeek機能、research preview
- 2026-09-01 朝 [TIPS] サブエージェント定義の`tools`と`model`をfrontmatterで絞る — `.claude/agents/*.md`で用途に応じたツール・モデル制限
- 2026-09-01 朝 [事例] Atlassian「Rovo」— ClaudeとGoogle Cloudで全社エージェント基盤、月間実行500万件超
- 2026-09-01 朝 [事例] 非エンジニアが5か月で社内ツール6本を本番稼働（Qiita、二次情報）— CONTEXT.md/SPEC.md/ADRで先に言語化、判断ロジックを純関数に分離
- 2026-09-01 朝 [速報] v2.1.252 Mac版task output swapエラー修正・settings.local.json不在時のalways allow修正・Remote Controlスタール修正・大容量バックグラウンド通知のAPIサイズ制限対応
- 2026-09-01 夕 [連載] 第5回 指示の粒度 — Delegate/dictateの境界、公式のbefore-after 4戦略、粒度を決める1基準、ターン途中で粒度を足す3経路
- 2026-09-01 夕 [TIPS] `/batch` は分割前に「計画の提示→承認」が入る — 投げっぱなしではない。単位はファイル数ではなく独立した作業量
- 2026-09-01 夕 [TIPS] 各サブエージェントはテストを走らせてからPRを開く — 手書き`claude -p`ループの自己申告OKとの差
- 2026-09-01 夕 [型] 情報源を指す — 「なぜこうなっているか」はgit履歴・PR・ログを名指しする。指さないとコードから推測される
- 2026-09-01 夕 [型] 既存パターンを指す — 手本のファイルを1つ名指しし、手段は委ねる（dictateにならないdelegate）
- 2026-09-01 夕 [TIPS] 差分を一文で説明できるなら計画は不要 — 計画が効くのは確信がない/複数ファイル/不慣れの3条件
- 2026-09-01 夕 [TIPS] 曖昧なプロンプトが正しい場面 — 探索中で方向修正の余裕があるとき（`what would you improve in this file?`）
- 2026-09-01 夕 [TIPS] The infinite exploration — スコープを切らない「調査して」でコンテキストが埋まる公式の失敗パターン
- 2026-09-01 夕 [TIPS] 実行中にEnterで送るとツール呼び出しは止まらない — キューに入り同じターン内で読まれる。入力欄1行目の`Up`で取り消し
- 2026-09-01 夕 [TIPS] `ultrathink` はキーワードとして認識される／`think`・`think hard`・`think more` は認識されない
- 2026-09-01 夕 [TIPS] `/effort` の6段階（low/medium/high/xhigh/max/ultracode）— `max`は考えすぎに陥りやすい。応答中にも変更可
- 2026-09-01 夕 [TIPS] 見ていない実行（定期実行・CI・`-p`）は聞き返せない — 成功条件と結果の扱いまで書き切る
- 2026-09-01 夕 [事例] Anthropic社内チームの粒度の使い分け — セキュリティ(TDD+チェックポイント)/デザイン(抽象+自律ループ)/データサイエンス(サンドボックスでワンショット)。分ける変数は「間違ったときに何を失うか」
- 2026-09-01 夕 [事例] 法務の電話応答ツリー試作・グロースマーケの広告バリエーション生成 — 非エンジニア部門には情報源を先に置くほうがプロンプト教育より効く
- 2026-09-01 夕 [用語] independent units（/batchの分解単位）/ Delegate, don't dictate / adaptive reasoning
- 2026-09-02 朝 [型] UI変更はスクリーンショット比較で検証させる — デザイン画像を渡し、実装後の結果を撮影・比較・差分列挙させてから直させる
- 2026-09-02 朝 [TIPS] 実装前に検証条件（テストケース）を渡す — 判定基準を先に渡すと確認の往復が減る
- 2026-09-02 朝 [TIPS] エラーメッセージはそのまま貼り根本原因を直させる — 抑制ではなく原因修正を明示する
- 2026-09-02 朝 [TIPS] `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`でサブエージェントのモデルを一括固定 — 個別のmodel指定を無視して全サブエージェントに強制適用（v2.1.257）
- 2026-09-02 朝 [事例] 楽天 — 市場投入までの時間24日→5日（79%減）、複雑なリファクタリングで7時間の自律コーディング、コード修正精度99.9%
- 2026-09-02 朝 [事例] Notion — Claude Managed Agentsで「External Agents」機能、公開3週間で1.8万エージェント作成・14万ステップ実行・9割が自動化トリガー
- 2026-09-02 朝 [速報] v2.1.257 Claude Fable 5.1追加（Fableの新デフォルト、1Mコンテキスト）・auto modeにContainment Escapeルール追加・`CLAUDE_CODE_SUBAGENT_MODEL_FORCE`追加・作業ディレクトリ外初回読み取り前の確認プロンプト追加
- 2026-09-02 朝 [速報] v2.1.258 macOS 12起動失敗の修正・リモート/予約セッションの権限承認エラー修正
- 2026-09-02 [BP] 起動レシピをリポジトリに記録して「動くところまで」検証させる — `/run-skill-generator` で `.claude/skills/run-<name>/` にレシピを記録し、`/run` `/verify` と他エージェントが同じ手順で起動する
- 2026-09-02 [連載] 第6回 差分の見せ方・レビューのさせ方 — `/code-review` の対象指定・effort の記憶・`--fix`/`--comment`/`--post`・背景実行・REVIEW.md と CLAUDE.md の非対称・ultra との使い分け
- 2026-09-02 [TIPS] `skillOverrides` で `code-review` を `user-invocable-only` にする — Claude の自発起動と定期タスクからの起動を止め、自分で打つぶんは残す
- 2026-09-02 [TIPS] スキル本文の `` !`コマンド` `` で差分を注入する — 探させずに確定した差分を渡す。置換は1回だけ、`!` は行頭か空白直後のみ
- 2026-09-02 [TIPS] 走っているレビューは `/tasks` で見る・止める — ultra を途中で止めると部分的な指摘は返らず無料枠だけ消費される
- 2026-09-02 [事例] Anthropic 社内の Code Review 実測 — 実質コメントの付く PR が 16%→54%、1,000行超は84%で平均7.5件、偽陽性1%未満、平均20分・$15〜25/PR
- 2026-09-02 [事例] GitHub Actions で3ペルソナ並列レビュー＋信頼スコア0.8で自動マージ（Qiita、二次情報）— 17%（DBスキーマ・認証・決済・インフラ）は人間必須、2週間のシャドーモードから段階導入
- 2026-09-02 [速報] Claude Code CLI は v2.1.258 から更新なし／Platform 9/1 のリリースノート（Mythos 5.1、キャッシュ読み取り $0.25/MTok、`tool_choice` の any・tool 非対応）
- 2026-09-02 [課題] 差分を固定してレビューさせるスキルを作る — `.claude/skills/review-diff/SKILL.md` に `!`git diff HEAD`` と3観点を書き、`/code-review low` と比較する
- 2026-09-02 [用語] バンドルスキル `/run` `/verify` `/run-skill-generator` / REVIEW.md / 重要度3段階（Important・Nit・Pre-existing）/ ultra の上限（500ファイル・8,000行）
- 2026-09-03 [BP] 捨てる前に書き出す（引き継ぎファイルと SessionStart フック）— `/handoff` スキルで `.claude/handoff/CURRENT.md` に書き出し、`SessionStart` の `startup`/`clear`/`compact` マッチャで自動的に読み直させる
- 2026-09-03 [連載] 第7回 うまくいかないときの立て直し方 — Esc / rewind / Summarize / branch / clear / compact の6手段は戻す対象が違う。チェックポイントの守備範囲、`/clear` は同一プロセス内なら rewind から戻せる
- 2026-09-03 [TIPS] `/clear` に名前を渡すと「離れる側」の会話に名前が付く — 引数なしだと新しい会話が名前を引き継ぐ（自動生成タイトルは引き継がない）
- 2026-09-03 [TIPS] `/branch` は許可グラントとバックグラウンド実行を引き継ぐ、`--fork-session` は別プロセスなので引き継がない
- 2026-09-03 [TIPS] `claude -p --resume <session-id> --output-format json` で終わったセッションに後から質問する — いまのコンテキストを汚さない
- 2026-09-03 [事例] Pictet（スイスのプライベートバンク）— 700人が Claude Code/Cowork を利用、25回のワークショップで500人以上を訓練、エンジニアから段階展開。コンプライアンス突合 3人で2週間→数時間
- 2026-09-03 [事例] `/handover` カスタムコマンドで引き継ぎを仕組み化（DevelopersIO、二次情報）— `~/.claude/commands/handover.md` と `.claude/handovers/`、「却下した案と理由」の節が効く
- 2026-09-03 [速報] v2.1.259 `managedMcpServers`・`--permission-prompts none`・同時セッションの相互巻き戻し修正・Bash `Read()` 拒否ルール強化・`allowedMcpServers` のスコープ変更・`claude plugin validate --json`・GitLab の `MR !N` 表示
- 2026-09-03 [課題] 引き継ぎがリセットをまたぐことを確かめる — `/handoff` → `/clear` → 新しい会話が状況を把握しているかを検証する
- 2026-09-03 [用語] SessionStart のマッチャ5種（startup/resume/clear/compact/fork）/ `disable-model-invocation` / チェックポイント100件・30日・`cleanupPeriodDays` / 圧縮後に再読込されるのは直近5ファイル
- 2026-09-04 [BP] 言語サーバーを繋いで編集直後に型エラーを Claude へ返す — `typescript-lsp@claude-plugins-official` と `typescript-language-server` バイナリ、`.claude/settings.json` の `enabledPlugins`、自動診断とコードナビゲーション
- 2026-09-04 [連載] 第8回 サブエージェント — 起動時に載るもの/載らないもの、`.claude/agents/` のフロントマター全体、`@agent-` 指名、フォーク（`/subtask`）、入れ子3層・同時20体、使う/使わないの判断フロー
- 2026-09-04 [TIPS] 使っていないプラグインを棚卸しする — Installed タブの「Not used recently」と Last used、`/plugin list --enabled`、`claude plugin details`
- 2026-09-04 [TIPS] `/reload-plugins` はプロンプトキャッシュを壊すと警告して止まる — `--force` で再実行。会話全体の再読込コストが発生する
- 2026-09-04 [TIPS] 子のツールは `tools`（許可リスト）より `disallowedTools`（引き算）で書く — MCP は `mcp__github` や `mcp__*` でも外せる。両方書くと disallowedTools が先
- 2026-09-04 [事例] DXC（保険基幹システム）— 保険部門1.4万人、オーケストレーション基盤「Assure」に Claude を4層で組み込み。請求受付のバックログ数日→数分、規制ルール組み込み12〜18か月→数日、労災計算アプリ8時間で構築・初回80%精度、人間の判断70%→20%
- 2026-09-04 [事例] サブエージェント定義は孫にも再利用される（Zenn / GENDA、二次情報）— `heavy-implementer` が指示なしに `code-explore` と `test-runner` を孫として呼んだ。記事の「5階層」は当時の記述で、現行の既定は3層
- 2026-09-04 [速報] 前回チェック以降の新規発表なし — CHANGELOG は v2.1.259 のまま、Platform リリースノートも 9/1 から更新なし
- 2026-09-04 [課題] Claude が自分の型エラーに同じターンで気づくか確かめる — Next.js で typescript-lsp を入れ、わざと型不一致を作らせて `tsc` なしで検出できるか見る
- 2026-09-04 [用語] code intelligence プラグイン / LSP ツール / 自動診断（Ctrl+O で閲覧）/ `enabledPlugins` のキー形式 / 対応表のバイナリ11言語 / クラウドセッションでは言語サーバーを起動しない
