#!/bin/bash

rm db.sqlite3
rm -rf ./coffeecrewapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations coffeecrewapi
python3 manage.py migrate coffeecrewapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

