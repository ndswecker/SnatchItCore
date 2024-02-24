#!/usr/bin/env bash

apt install python3-venv -y

python3 -m venv /srv/web/venv
/srv/web/venv/bin/python3 -m pip install pip setuptools wheel --upgrade --no-cache-dir
/srv/web/venv/bin/python3 -m pip install -r /srv/web/requirements/prod.txt --upgrade --no-cache-dir
cp /srv/web/envs/prod.env /srv/web/.env
SECRET_KEY=$(python3 -c "import secrets;print(secrets.token_urlsafe(64))")
sed -i "s/<SECRET_KEY>/$SECRET_KEY/g" /srv/web/.env
/srv/web/venv/bin/python3 /srv/web/app/manage.py collectstatic
/srv/web/venv/bin/python3 /srv/web/app/manage.py migrate
