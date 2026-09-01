# Artifact テンプレートの使い方

`template/digest.html` を**必ず出発点**にしてください。CSS は触らず、`<div class="paper">` の中身だけを差し替えます。
デザインは固定です。毎回作り直すとブレるので、`artifact-design` スキルを読み込む必要はありません。

## 使えるクラス

| 用途 | 書き方 |
|---|---|
| 3行サマリー | `<div class="lede"><p>…</p>…</div>` |
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

## 注意

- コードは `<pre><code>` に入れる。**01 の節ではコードブロックを省かない**（この節の存在理由がコードと図です）。
- Mermaid のラベルは必ず `["…"]` とダブルクォートで囲む。`()` `:` `,` が裸で入ると描画に失敗します。
- 図は `<pre class="mermaid">` の中に**インデントなし**で書く（先頭の空白でパースが崩れることがある）。
- 題字の日付・号数・読了目安（`.masthead-meta`）を毎回更新すること。読了目安は 12〜15分。
- HTML の先頭は `<title>Claude Daily</title>` のまま変えない（タブとギャラリーでの名前が毎回変わると別物に見えるため）。
