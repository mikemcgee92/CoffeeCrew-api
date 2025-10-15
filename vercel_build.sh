#!/bin/bash
set -e

echo "Build script started..."

echo "Python version:"
python --version

echo "Installing Python dependencies..."
pip install -r requirements-dev.txt

# Set Django settings module to production
export DJANGO_SETTINGS_MODULE=coffeecrew.production_settings

# Test database connection
echo "Testing database connection..."
python << END
import os
import sys
import django
from django.db import connections
from django.db.utils import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeecrew.production_settings')
django.setup()

try:
    connection = connections['default']
    connection.cursor()
    print("Database connection successful!")
except OperationalError as e:
    print(f"Database connection failed: {e}")
    sys.exit(1)
END

echo "Running Django migrations..."
python manage.py showmigrations
python manage.py migrate --noinput --verbosity 2

echo "Verifying tables..."
python << END
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeecrew.production_settings')
django.setup()

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    tables = cursor.fetchall()
    print("Available tables:")
    for table in tables:
        print(f"- {table[0]}")
END

echo "Loading initial data..."
python manage.py loaddata category ingredient recipe --verbosity 2

echo "Collecting static files..."
python manage.py collectstatic --noinput --verbosity 2

echo "Build script completed!"
