"""
WSGI config for Vercel deployment
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
app_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_path)

# Use production settings for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeecrew.production_settings')

try:
    # Initialize Django WSGI application
    app = get_wsgi_application()
except Exception as e:
    print(f"Error loading the application: {e}")
    raise
