#!/usr/bin/env bash

apt install python3-venv -y

python3 -m venv /srv/web/venv
/srv/web/venv/bin/python3 -m pip install pip setuptools wheel --upgrade --no-cache-dir
/srv/web/venv/bin/python3 -m pip install -r /srv/web/requirements/prod.txt --upgrade --no-cache-dir

/srv/web/venv/bin/python3 /srv/web/app/manage.py collectstatic
/srv/web/venv/bin/python3 /srv/web/app/manage.py migrate
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_bands /srv/web/data/Bands.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_ageannuals /srv/web/data/AgeAnnuals.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_agewrps /srv/web/data/AgeWRPs.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_groupwrps /srv/web/data/GroupWRPs.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_species /srv/web/data/TaxonBBL.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_band_allocations /srv/web/data/BandAllocations.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py setup_taxon_band_relationships
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_morphometrics /srv/web/data/Morphometrics.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py setup_taxon_relationships

cp /srv/web/deploy/adhoc/django.service /etc/systemd/system/django.service
cp /srv/web/deploy/adhoc/django.timer /etc/systemd/system/django.socket
systemctl daemon-reload
systemctl start django.timer
systemctl enable django.timer
