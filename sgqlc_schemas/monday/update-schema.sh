#!/bin/sh

if [ -z "$MONDAY_TOKEN" ]; then
    echo "please export MONDAY_TOKEN with your Monday.com API token" >&2
    exit 1
fi

python3 \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    -H "Authorization:${MONDAY_TOKEN}" \
    https://api.monday.com/v2 \
    monday_schema.json || exit 1

sgqlc-codegen monday_schema.json __init__.py
