#!/bin/sh
set -eu
rm -rf dist
mkdir -p dist/server dist/client
cp index.html app.js config.js style.css out/
cp -R out/. dist/client/
rm -f dist/client/index.html dist/client/app.js dist/client/config.js dist/client/style.css dist/client/cover-status.json dist/client/_routes.json
node build_worker.mjs
