#!/bin/bash
echo "Installing dependencies..."
python3.9 -m pip install --upgrade pip
python3.9 -m pip install --no-cache-dir -r requirements.txt

echo "Running collectstatic..."
python3.9 manage.py collectstatic --no-input --clear
