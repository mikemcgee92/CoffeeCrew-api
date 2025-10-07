#!/bin/bash
set -e

echo "Installing Python dependencies..."
pip install -r requirements-dev.txt

echo "Running Django migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput
