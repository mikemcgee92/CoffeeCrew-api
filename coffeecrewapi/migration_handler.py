import os
import django
from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError

def apply_migrations():
    """Apply database migrations and load initial data."""
    try:
        # Test database connection
        connection = connections['default']
        connection.cursor()
        
        # Apply migrations
        call_command('migrate', '--noinput', verbosity=2)
        
        # Check if we need to load initial data
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM coffeecrewapi_recipe")
            count = cursor.fetchone()[0]
            
        if count == 0:
            # Load initial data if no recipes exist
            print("Loading initial data...")
            call_command('loaddata', 'category', 'ingredient', 'recipe', verbosity=2)
            
    except OperationalError as e:
        print(f"Database error: {e}")
        raise
    except Exception as e:
        print(f"Error during migration: {e}")
        raise
