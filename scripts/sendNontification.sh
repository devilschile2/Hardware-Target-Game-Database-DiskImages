#!/bin/bash

echo "Notifying..."


TOKEN=token:token

CHAT_ID=14950119
URL="https://api.telegram.org/bot$TOKEN/sendMessage"


curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$1"
echo ""
