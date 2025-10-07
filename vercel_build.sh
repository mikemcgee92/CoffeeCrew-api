#!/bin/bash
set -e

echo "Installing Python dependencies..."
pip install -r requirements-dev.txt

# Set Django settings module to production
export DJANGO_SETTINGS_MODULE=coffeecrewproject.production_settings

echo "Running Django migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput
