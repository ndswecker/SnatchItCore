# Deploy

Deploy a Python web application to a Debian server with Django and Gunicorn installed in a virtual environment, a Postgres database, NGINX as a reverse proxy and static file server. Secure the server with UFW, and set up TLS with Certbot. Establish continuous delivery using GitHub actions and a webhook.

## Provision server instance

Use your preferred cloud provider to create a Debian VM instance. Enable HTTP/HTTPS traffic in the firewall.

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
- https://cloud.google.com/compute/docs/instances/create-start-instance

## Clone repository and install

```shell
sudo apt update
sudo apt upgrade -y
sudo apt install git -y
sudo git clone https://github.com/ndswecker/SnatchItCore.git /srv/web
sudo bash /srv/web/deploy/install.sh
sudo /srv/web/venv/bin/python3 /srv/web/app/manage.py createsuperuser
```

## Update

```shell
sudo bash /srv/web/deploy/update.sh
```

### Private repository

You will need an access token if the repository is private.

1. https://github.com/settings/tokens/new
1. Select `repo` scope
1. Generate
1. Copy token
1. Enter the token as your password when prompted by git to authenticate

Include GitHub credentials to bypass interactive prompt

```shell
sudo apt install git -y
sudo git clone https://USERNAME:ACCESS_TOKEN@github.com/harrelchris/bp-django.git /srv/web
sudo bash /srv/web/deploy/install.sh
```

## Logs

```shell
# NGINX
journalctl -u nginx.service
tail /var/log/nginx/access.log
tail /var/log/nginx/error.log

# Gunicorn
journalctl -u gunicorn.socket

# Application
journalctl -u gunicorn.service

# Postgres
/var/log/postgresql/postgresql-13-main.log

# Timers
systemctl list-timers
systemctl --type=timer --all --failed

systemctl status example.timer
journalctl -u example.timer
```

## Install timer

Add to `deploy/install.sh`

```shell
sudo cp /srv/web/deploy/timers/example.service /etc/systemd/system/example.service
sudo cp /srv/web/deploy/timers/example.timer /etc/systemd/system/example.timer
sudo systemctl enable example.timer --now
```
