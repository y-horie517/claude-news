# Artifact テンプレートの使い方

`template/digest.html` を**必ず出発点**にしてください。CSS は触らず、`<div class="paper">` の中身だけを差し替えます。
デザインは固定です。毎回作り直すとブレるので、`artifact-design` スキルを読み込む必要はありません。

## 版の切り替え

- 朝刊: `<div class="paper" data-edition="am">` ＋ `<span class="edition">朝刊</span>`
- 夕刊: `<div class="paper" data-edition="pm">` ＋ `<span class="edition">夕刊</span>`

アクセント色が自動で切り替わります（朝＝縹色の青／夕＝蘇芳の赤）。

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

**朝刊**: 01 推奨される使い方 / 02 開発TIPS / 03 最新事例 / 04 速報 / 05 きょうの課題
**夕刊**: 01 答え合わせ / 02 深掘り連載 / 03 ケーススタディ / 04 チートシート / 05 あすの予告

## 注意

- Mermaid のラベルは必ず `["…"]` とダブルクォートで囲む。`()` `:` `,` が裸で入ると描画に失敗します。
- 図は `<pre class="mermaid">` の中に**インデントなし**で書く（先頭の空白でパースが崩れることがある）。
- 題字の日付・号数・読了目安（`.masthead-meta`）を毎回更新すること。
- HTML の先頭は `<title>Claude Daily</title>` のまま変えない（タブとギャラリーでの名前が毎回変わると別物に見えるため）。
