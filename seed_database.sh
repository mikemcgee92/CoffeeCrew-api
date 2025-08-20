#!/bin/bash

rm db.sqlite3
rm -rf ./coffeecrewapi/migrations
python manage.py makemigrations coffeecrewapi
python manage.py migrate
python manage.py loaddata category
python manage.py loaddata recipe
python manage.py loaddata ingredient
python manage.py loaddata ingredient_amount
