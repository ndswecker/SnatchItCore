#!/usr/bin/env bash

# Update
apt update
apt upgrade -y

# Install dependencies
apt install nginx postgresql python3-venv ufw -y

# Configure UFW
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

# Create database
sudo -u postgres psql -c "CREATE USER web WITH ENCRYPTED PASSWORD 'pass';"
sudo -u postgres psql -c "CREATE DATABASE web;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE web TO web;"

# Install application
python3 -m venv /srv/web/venv
/srv/web/venv/bin/python3 -m pip install pip setuptools wheel --upgrade --no-cache-dir
/srv/web/venv/bin/python3 -m pip install -r /srv/web/requirements/prod.txt --upgrade --no-cache-dir
cp /srv/web/envs/prod.env /srv/web/.env
SECRET_KEY=$(python3 -c "import secrets;print(secrets.token_urlsafe(64))")
sed -i "s/<SECRET_KEY>/$SECRET_KEY/g" /srv/web/.env
/srv/web/venv/bin/python3 /srv/web/app/manage.py collectstatic
/srv/web/venv/bin/python3 /srv/web/app/manage.py migrate

# Create gunicorn socket and service
cp /srv/web/deploy/gunicorn.service /etc/systemd/system/gunicorn.service
cp /srv/web/deploy/gunicorn.socket /etc/systemd/system/gunicorn.socket
systemctl daemon-reload
systemctl start gunicorn.socket
systemctl enable gunicorn.socket

# Configure NGINX
cp /srv/web/deploy/app.conf /etc/nginx/conf.d/app.conf
PUBLIC_IP=$(curl -s -4 ifconfig.me)
sed -i "s/server_name ~^.+$;/server_name $PUBLIC_IP;/" /etc/nginx/conf.d/app.conf
systemctl restart nginx
