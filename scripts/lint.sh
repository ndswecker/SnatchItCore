#!/usr/bin/env bash

source .venv/bin/activate

python3 -m black app --line-length 120 --exclude migrations/

python3 -m flake8 app
