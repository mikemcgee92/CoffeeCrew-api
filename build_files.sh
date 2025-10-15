#!/bin/bash

# Exit on error
set -e

# Install Python and pip if not available
if ! command -v python3.9 &> /dev/null; then
    echo "Python 3.9 not found. Installing..."
    apt-get update && apt-get install -y python3.9
fi

# Create and activate virtual environment
python3.9 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements-dev.txt

echo "Running collectstatic..."
python manage.py collectstatic --noinput
