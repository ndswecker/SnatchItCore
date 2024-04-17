@echo off

:: Create virtual environment
if not exist .venv\ (
	python -m venv .venv
)

:: Activate virtual environment
call .venv\Scripts\activate

:: Update virtual environment
python -m pip install pip setuptools wheel --upgrade

:: Install dependencies
pip install -r requirements/dev.txt --upgrade

:: Create .env from example
if not exist .env (
	copy .\envs\dev.env .env
)

:: Delete the existing database
if exist db.sqlite3 (
	del db.sqlite3
)

:: Initialize a clean database
python app\manage.py makemigrations
python app\manage.py migrate


:: python app\manage.py createsuperuser --username user --email user@email.com --noinput
python app\manage.py loaddata users-dev

:: Load initial data
python app\manage.py import_bands .\data\Bands.csv
python app\manage.py import_ageannuals .\data\AgeAnnuals.csv
python app\manage.py import_agewrps .\data\AgeWRPs.csv
python app\manage.py import_groupwrps .\data\GroupWRPs.csv