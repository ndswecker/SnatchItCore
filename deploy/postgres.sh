#!/usr/bin/env bash

apt install postgresql -y

sudo -u postgres psql -c "CREATE DATABASE web;"
sudo -u postgres psql -c "CREATE USER \"www-data\" WITH ENCRYPTED PASSWORD 'pass';"
sudo -u postgres psql -c "ALTER DATABASE web OWNER TO \"www-data\";"
