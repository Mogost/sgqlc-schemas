#!/bin/sh

if [ -z "$GITHUB_TOKEN" ]; then
    echo "please export GITHUB_TOKEN with your GitHub API token" >&2
    echo "see: https://github.com/settings/tokens" >&2
    exit 1
fi

python3 \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    -H "Authorization: bearer ${GITHUB_TOKEN}" \
    https://api.github.com/graphql \
    schema.json || exit 1

sgqlc-codegen schema.json __init__.py
