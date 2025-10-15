#!/bin/bash
set -e

echo "Build script started..."

echo "Python version:"
python --version

echo "Installing Python dependencies..."
pip install -r requirements-dev.txt

# Set Django settings module to production
export DJANGO_SETTINGS_MODULE=coffeecrew.production_settings

echo "Collecting static files..."
python manage.py collectstatic --noinput --verbosity 2

echo "Build script completed!"
