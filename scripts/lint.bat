@echo off

call .venv\Scripts\activate

python -m black app --line-length 120 --exclude migrations/

python -m flake8 app
