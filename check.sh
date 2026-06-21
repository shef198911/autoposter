#!/usr/bin/env sh
cd "$(dirname "$0")"
python3 app.py self-test
python3 app.py status
