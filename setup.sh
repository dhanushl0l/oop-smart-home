#!/usr/bin/env bash
set -e 

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Virtual environment created."
fi

source .venv/bin/activate

python main.py