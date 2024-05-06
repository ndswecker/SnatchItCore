#!/usr/bin/env bash

cd /srv/web/
git pull
/srv/web/venv/bin/python3 /srv/web/app/manage.py collectstatic --noinput
/srv/web/venv/bin/python3 /srv/web/app/manage.py migrate --noinput

/srv/web/venv/bin/python3 /srv/web/app/manage.py import_bands /srv/web/data/Bands.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_ageannuals /srv/web/data/AgeAnnuals.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_agewrps /srv/web/data/AgeWRPs.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_groupwrps /srv/web/data/GroupWRPs.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_species /srv/web/data/TaxonBBL.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_band_allocations /srv/web/data/BandAllocations.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py setup_taxon_band_relationships
/srv/web/venv/bin/python3 /srv/web/app/manage.py import_morphometrics /srv/web/data/Morphometrics.csv
/srv/web/venv/bin/python3 /srv/web/app/manage.py setup_taxon_relationships

systemctl stop gunicorn.socket
systemctl stop gunicorn.service
# systemctl stop ufw
systemctl stop nginx

systemctl daemon-reload
systemctl start gunicorn.socket
systemctl enable gunicorn.socket
# systemctl restart ufw
systemctl restart nginx
