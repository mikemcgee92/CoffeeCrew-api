"""
WSGI config for Vercel deployment
"""
import os
from django.core.wsgi import get_wsgi_application

# Use production settings for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeecrewproject.production_settings')

# Initialize Django WSGI application
app = get_wsgi_application()
