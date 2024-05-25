#!/usr/bin/env bash

cp /srv/web/deploy/adhoc/django.service /etc/systemd/system/django.service
cp /srv/web/deploy/adhoc/django.timer /etc/systemd/system/django.socket
systemctl daemon-reload
systemctl start django.timer
systemctl enable django.timer
