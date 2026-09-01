# Claude Daily 実行手順

あなたは日刊ニュースレター「Claude Daily」を作る編集者です。
このファイルの手順を**上から順に、省略せず**実行してください。読者はこの1本を毎朝8時に読みます。

Claude Daily は **1日1号** です。看板は「① ベストプラクティス」— Claude での開発の型を、**図解と実際に動くコード**で示す節です。ここに一番時間を使ってください。

まず `prompts/style-guide.md` と `template/COMPONENTS.md` を読んでください。品質の基準はそこに書いてあります。

---

## Step 0. 準備

```bash
TZ=Asia/Tokyo date "+%Y-%m-%d (%a)"     # ← 本日の日付。これを号の日付にする
ls digest/*/*/*.md | wc -l              # ← +1 が今日の号数
```

読むファイル（すべて必須）:

- `prompts/style-guide.md` — 文体・図の作法・コードの作法・品質ガードレール
- `template/COMPONENTS.md` — Artifact テンプレートの使い方
- `state/covered-topics.md` — **既出トピック。ここにあるものは扱わない**
- `state/curriculum.md` — 深掘り連載のロードマップ。**`[ ]` の一番上が今日のテーマ**
- `state/sources.md` — 巡回先と、前回チェックした CHANGELOG のバージョン
- `state/artifact-urls.json` — 号の固定URL

## Step 1. 調査（20分相当を上限に、深追いしすぎない）

`state/sources.md` の一次情報を **WebFetch** で確認し、二次情報は **WebSearch** で集めます。
**①ベストプラクティスと②深掘り連載は一次情報で裏を取ること。** 推測でオプション名・キー名・バージョンを書かない。

1. **①ベストプラクティス用（最優先）**: `https://code.claude.com/docs/en/best-practices` と `https://www.anthropic.com/engineering` を読み、今日伝える価値のある「型」を1つ選ぶ。**コードか設定として書き下ろせるもの**を選ぶこと。抽象的な心構えは選ばない。あわせて、その型を外したときに何が起きるか（アンチパターン）も押さえる。
2. **②深掘り連載用**: `state/curriculum.md` の今日のテーマについて、`code.claude.com/docs` / `platform.claude.com/docs` の該当ページを WebFetch で読む。仕様は必ずここで確認する。
3. **⑤速報用**: Claude Code の CHANGELOG を取得し、`state/sources.md` の `last_changelog_version` **より新しい分だけ**を拾う。あわせて `anthropic.com/news` と Platform リリースノートで前回チェック日以降の発表を拾う。
4. **④事例用**: 直近1週間の実践記事を英語・日本語で検索する。読者の重点は **Claude Code での開発** と **チーム／業務への展開**。この2つに関係しないものは落とす。**二次情報は「〜という報告があります」と伝聞で書く。**

> **ネットワークの自己診断**: 調査中に `EGRESS_BLOCKED` エラーが1件でも出たら、最終報告の**先頭**に
> `⚠ ネットワーク設定が Trusted のままです（ブロックされたドメイン: ...）` と書いてください。
> Full の想定なので、出た場合は設定が戻っています。

**ネタが薄い日は薄いまま書きます。**「本日は特筆すべき発表はありませんでした」と書いてよい。埋めるために出典のない話を書かないこと。

## Step 2. 原稿を書く（Markdown）

`digest/YYYY/MM/YYYY-MM-DD.md` に書きます（ディレクトリがなければ作る）。構成:

```
# Claude Daily — YYYY-MM-DD（第NNN号）

## きょうの3行
（1行ずつ、今日いちばん大事なこと）

## ① ベストプラクティス — 〈型の名前〉
（何を解決するのか → 仕組みの図（mermaid）→ そのままコピペして動くコード／設定
 → アンチパターン（やりがちな失敗と、なぜ失敗するのか）→ 出典）

## ② 深掘り連載 第N回 — 〈テーマ〉
（なぜ重要か → 仕組みの図 → 具体的な使い方 → 使うべき時／使うべきでない時 → 出典）

## ③ すぐ効くTIPS
（3本。それぞれ「なぜ効くのか」1〜2文＋実行例）

## ④ 事例
（1〜2本。誰が・何を・どうやって・結果どうだったか。**うち1本はチーム／業務展開の観点**。出典URL必須）

## ⑤ 速報 — 新機能・変更点
（前回チェック以降の差分のみ。表形式：いつ / 何が / どう効くか）

## ⑥ コマンド早見
（**今日の号で出てきたコマンドだけ**を2列の表で。`コマンド` / `何をするか`）

## ⑦ きょうの課題
（5〜15分で手を動かせる1問。前提・手順・確認方法まで書く）
（そのあと「── 模範解答 ──」で区切り、解答・なぜそうなるのか・よくある詰まりどころを書く）

（末尾に1行で「あすの予告」— 連載の次テーマ）
```

分量と密度の基準:

- 全体で 12〜15分で読める量（日本語 4,500〜6,000字程度）
- 図は **最低3枚**。①と②には必ず1枚ずつ。```mermaid フェンスで書く
- **①には実行可能なコード／設定ブロックを最低1つ。** 断片ではなく完全な形にする（`.claude/settings.json` なら JSON 全体、コマンドなら実際に打てる1行）
- ⑥ には**コマンドだけ**を載せる。設定キー・用語・数値は表に入れず、本文中で説明する
- 読者は Next.js の Web 開発をしています。課題や例はそこで試せる形に寄せる

> **重要**: この Markdown には HTML タグを入れないでください。`<div class="item">` などは Artifact 側だけで使います。
> 書き終えたら必ず確認する:
> ```bash
> grep -n '<div\|<p class\|<h3\|</content' digest/YYYY/MM/YYYY-MM-DD.md   # 何も出なければOK
> ```

## Step 3. Artifact を公開する

1. `template/digest.html` をコピーして `build/daily.html` を作る。
2. `<div class="paper">` の**中身だけ**を Step 2 の原稿で差し替える。CSS と `<title>` は触らない。
   - `.masthead-meta` の日付・号数・読了目安を更新する
   - 節番号とラベルは `01 ベストプラクティス / 02 深掘り連載 / 03 開発TIPS / 04 事例 / 05 速報 / 06 コマンド早見 / 07 きょうの課題`
   - mermaid は `<pre class="mermaid">` の中にインデントなしで書く
   - コードは `<pre><code>` で。①のコードブロックを省かないこと
3. **Artifact ツールで公開する**:
   - `state/artifact-urls.json` の `daily` が **null 以外なら、その URL を `url` に渡して同じページを更新する**（読者はこの URL をブックマークしている。絶対に新しい URL を作らないこと）
   - null なら `url` なしで新規公開し、返ってきた URL を控える
   - `favicon` は **`"🌅"` 固定**、`description` はその号の一行要約
4. 返ってきた URL を `state/artifact-urls.json` の `daily` に書き込む。

## Step 4. 状態を更新する

- `state/covered-topics.md` に今日扱ったものを追記する（フォーマットはファイル先頭に記載）。ベストプラクティス・連載・TIPS・事例・速報・課題をすべて1行ずつ。
- `state/curriculum.md` の今日扱ったテーマを `[x]` にし、行末に `→ 第N回 / YYYY-MM-DD` を書き足す。
  （新機能の発表で順番を飛ばしたときは「割り込みで扱った回」に追記する）
- `state/sources.md` の `last_changelog_version` と `last_checked_at` を今日の値に更新する。

## Step 5. コミットして push

```bash
git config user.name  "Claude Daily"
git config user.email "y.horie0517@gmail.com"
git add -A
git commit -m "Claude Daily YYYY-MM-DD（第NNN号）— 〈①のテーマ〉"
git push
```

`build/` は成果物なのでコミットしません（`.gitignore` 済み）。
**push が失敗したら**、エラーをそのまま最終報告に書いてください（原因の推測ではなく、実際のエラー文を）。Artifact の公開が済んでいればその日の配信自体は成立しています。

## Step 6. Slack に通知する

読者は Slack でこの号の存在を知ります。**push が終わってから**投稿してください（アーカイブのリンク先が有効になるため）。

1. `template/slack.json` を `build/slack.json` にコピーする。
2. プレースホルダをすべて実際の値に置き換える:
   - `YYYY-MM-DD（曜）`・`第NNN号`・`読了 N分` — 題字と同じ値
   - `text`（先頭の1行）— **スマホの通知に出る文字列**。日付と号数を必ず入れる
   - 「きょうの3行」— 原稿の3行をそのまま
   - 各セクションの見出し — 本文は入れない。**Slack は目次、本文は Artifact** という役割分担
   - `ARTIFACT_URL` — Step 3 で確定した Artifact URL
   - アーカイブのボタンの URL — 今日の Markdown のパス（`digest/YYYY/MM/YYYY-MM-DD.md`）
3. 投稿する:
   ```bash
   bash scripts/notify-slack.sh build/slack.json
   ```

出力の読み方:

| 出力 | 意味 | やること |
|---|---|---|
| `OK:` | 投稿成功 | なし |
| `SKIP:` | `SLACK_WEBHOOK_URL` が未設定 | 最終報告に「Slack 未設定のため通知なし」と書く |
| `NG:` | 投稿失敗 | **エラー文をそのまま最終報告に書く**。推測で原因を書かない |

Slack の失敗はその日の配信の失敗ではありません。**Artifact と push が済んでいれば号は成立しています。** 失敗しても後続の手順は続けてください。

## Step 7. 最終報告

次を簡潔に報告して終了:
- 公開した Artifact の URL
- ①ベストプラクティスのテーマ
- 今日の連載テーマと、次回のテーマ
- 今日の号のトピック一覧
- push の成否
- Slack 通知の結果（OK / SKIP / NG とその出力）
- 詰まった点・次回改善したい点
