#!/usr/bin/env bash

# Create virtual environment
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Update virtual environment
python3 -m pip install pip setuptools wheel --upgrade

# Install dependencies
pip install -r requirements/dev.txt --upgrade

# Create .env from example
if [ ! -f ".env" ]; then
    cp ./envs/dev.env .env
fi

# Delete the existing database
if [ -f "db.sqlite3" ]; then
    rm db.sqlite3
fi

# Initialize a clean database
python app/manage.py makemigrations
python app/manage.py migrate

python app/manage.py createsuperuser --username user --email user@email.com --noinput
