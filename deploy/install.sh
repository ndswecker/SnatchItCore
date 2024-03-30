#!/usr/bin/env bash

# Configure UFW
# source /srv/web/deploy/ufw.sh

# Create database
source /srv/web/deploy/postgres.sh

# Install application
source /srv/web/deploy/app.sh

# Create gunicorn socket and service
source /srv/web/deploy/gunicorn.sh

# Configure NGINX
source /srv/web/deploy/nginx.sh
