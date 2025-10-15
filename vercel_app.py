"""
WSGI config for Vercel deployment
"""
import os
import sys
from pathlib import Path

# Get the project root directory and add it to the Python path
current_dir = Path(__file__).resolve().parent
project_root = str(current_dir)
sys.path.insert(0, project_root)

# Use production settings for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeecrew.production_settings')

# Initialize Django before importing migration_handler
import django
django.setup()

from coffeecrewapi.migration_handler import apply_migrations
from django.core.wsgi import get_wsgi_application

try:
    # Apply migrations first
    print("Applying migrations...")
    apply_migrations()
    print("Migrations completed successfully")
    
    # Initialize Django WSGI application
    app = get_wsgi_application()
except Exception as ex:
    print(f"Error during startup: {str(ex)}")
    print(f"Current directory: {project_root}")
    print(f"Directory contents: {os.listdir(project_root)}")
    print(f"Python path: {sys.path}")
    print(f"Environment: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    raise
