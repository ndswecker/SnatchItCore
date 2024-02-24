#!/usr/bin/env bash

apt install ufw -y

ufw --force disable
ufw --force reset
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow http
ufw allow https
sed -i "s/IPV6=no/IPV6=yes/" /etc/default/ufw
ufw --force disable
ufw --force enable
systemctl restart ufw
