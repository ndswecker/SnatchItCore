#!/usr/bin/env bash

source /srv/web/deploy/postgres.sh

apt install python3-venv -y

python3 -m venv /srv/web/venv
/srv/web/venv/bin/python3 -m pip install pip setuptools wheel --upgrade --no-cache-dir
/srv/web/venv/bin/python3 -m pip install -r /srv/web/requirements/prod.txt --upgrade --no-cache-dir

/srv/web/venv/bin/python3 /srv/web/app/manage.py collectstatic --noinput
/srv/web/venv/bin/python3 /srv/web/app/manage.py migrate

cp /srv/web/deploy/adhoc/django.service /etc/systemd/system/django.service
cp /srv/web/deploy/adhoc/django.timer /etc/systemd/system/django.timer
systemctl daemon-reload
systemctl start django.timer
systemctl enable django.timer
