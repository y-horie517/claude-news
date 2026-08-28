#!/usr/bin/env bash
# Slack Incoming Webhook にペイロードを投げる。
#
#   scripts/notify-slack.sh build/slack.json
#
# Webhook URL はクラウド環境の環境変数 SLACK_WEBHOOK_URL から読みます。
# リポジトリは public なので、URL を絶対にファイルに書かないこと。
set -uo pipefail

payload="${1:-}"

if [ -z "$payload" ]; then
  echo "usage: $0 <payload.json>" >&2
  exit 2
fi

if [ ! -f "$payload" ]; then
  echo "NG: ペイロードが見つかりません: $payload" >&2
  exit 2
fi

# JSON として妥当かを先に確認する（壊れた JSON は Slack 側で invalid_payload になる）
if ! python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$payload" 2>/dev/null; then
  echo "NG: $payload が正しい JSON ではありません" >&2
  exit 2
fi

if [ -z "${SLACK_WEBHOOK_URL:-}" ]; then
  echo "SKIP: 環境変数 SLACK_WEBHOOK_URL が未設定のため Slack 通知を飛ばしました。"
  echo "      設定場所: claude.ai/code → 雲アイコン → 環境の歯車 → Environment variables"
  exit 0
fi

# Slack は成功時に本文 "ok" を返す
response=$(curl -sS --max-time 20 -X POST \
  -H 'Content-type: application/json' \
  --data @"$payload" \
  "$SLACK_WEBHOOK_URL" 2>&1)
status=$?

if [ $status -ne 0 ]; then
  echo "NG: curl が失敗しました (exit $status): $response" >&2
  exit 1
fi

if [ "$response" = "ok" ]; then
  echo "OK: Slack に投稿しました。"
  exit 0
fi

echo "NG: Slack がエラーを返しました: $response" >&2
exit 1
