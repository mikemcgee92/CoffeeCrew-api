"""
WSGI config for Vercel deployment
"""
import os
import sys
from pathlib import Path

# Get the project root directory
current_dir = Path(__file__).resolve().parent
project_root = str(current_dir)

# Add the project root and its parent to the Python path
sys.path.insert(0, project_root)
sys.path.insert(0, str(current_dir.parent))

# Print debug information
print(f"Project root: {project_root}")
print(f"Current directory contents: {os.listdir(project_root)}")
print(f"Python path: {sys.path}")

# Use production settings for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeecrew.production_settings')

# Initialize Django
import django
django.setup()

try:
    # Import and initialize migration handler
    from coffeecrewapi.migration_handler import apply_migrations
    print("Running migrations...")
    apply_migrations()
    print("Migrations completed")
    
    # Get WSGI application
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
    print("WSGI application initialized successfully")
    
except Exception as ex:
    print(f"Error during startup: {str(ex)}")
    print(f"Current directory: {project_root}")
    print(f"Directory contents: {os.listdir(project_root)}")
    print(f"Parent directory contents: {os.listdir(current_dir.parent)}")
    print(f"Python path: {sys.path}")
    print(f"Environment vars: {dict(os.environ)}")
    raise
