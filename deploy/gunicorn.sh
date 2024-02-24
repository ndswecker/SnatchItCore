#!/usr/bin/env bash

cp /srv/web/deploy/gunicorn.service /etc/systemd/system/gunicorn.service
cp /srv/web/deploy/gunicorn.socket /etc/systemd/system/gunicorn.socket
systemctl daemon-reload
systemctl start gunicorn.socket
systemctl enable gunicorn.socket
