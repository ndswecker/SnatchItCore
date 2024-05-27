# Ad-Hoc

How to run the Django Application on a Raspberry Pi in an Ad-Hoc network

## Get current secret key

1. SSH into prod
1. Read .env

```shell
cat /srv/web/.env
```

1. Copy secret key to your PC

## Download prod data

1. Dump data

```shell
sudo -E /srv/web/venv/bin/python3 /srv/web/app/manage.py dumpdata -o ~/snatchitcore.json
```

1. Download the file using Google Cloud SSH client

## Transfer `snatchitcore.json` to Raspberry pi

1. Use Filezilla

## Install

1. Clone repo to pi

```shell
sudo apt update
sudo apt upgrade -y
sudo apt install git -y
sudo git clone https://github.com/ndswecker/SnatchItCore.git /srv/web
```

1. Copy `prod.env` and update `SECRET_KEY`

```shell
sudo cp /srv/web/envs/prod.env /srv/web/.env
sudo nano /srv/web/.env
# Paste in SECRET_KEY from production that you copied previously
```

1. Install the application

```shell
sudo bash /srv/web/deploy/adhoc/install.sh
```

1. Insert data from prod

```shell
sudo bash /srv/web/venv/bin/python3 /srv/web/app/manage.py loaddata ~/snatchitcore.json
```
