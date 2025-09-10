# CoffeeCrew API

A Django REST Framework API for managing coffee recipes and their ingredients. This API serves as the backend for the CoffeeCrew application, allowing users to create and manage coffee recipes.

## Features

- Full CRUD operations for coffee recipes
- Category management for recipe organization
- Ingredient tracking with amounts and measurements
- Cross-Origin Resource Sharing (CORS) enabled for frontend integration

## Tech Stack

- Python 3.9
- Django
- Django REST Framework
- SQLite3 (Development Database)
- django-cors-headers
- Square

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Pipenv

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mikemcgee92/CoffeeCrew-api.git
   cd CoffeeCrew-api
   ```

2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Apply database migrations & load fixtures:
   ```bash
   ./seed_data.sh
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Recipes

- `GET /recipes` - List all recipes
- `GET /recipes/{id}` - Retrieve a specific recipe
- `POST /recipes` - Create a new recipe
- `PUT /recipes/{id}` - Update a recipe
- `DELETE /recipes/{id}` - Delete a recipe
- `POST /recipes/{id}/ingredient` - Add an ingredient to a recipe
- `DELETE /recipes/{id}/ingredient` - Remove an ingredient from a recipe

### Categories

- `GET /categories` - List all categories
- `GET /categories/{id}` - Retrieve a specific category
- `POST /categories` - Create a new category
- `PUT /categories/{id}` - Update a category
- `DELETE /categories/{id}` - Delete a category

### Ingredients

- `GET /ingredients` - List all ingredients
- `GET /ingredients/{id}` - Retrieve a specific ingredient

### Square
- `GET /square/orders` - List orders from Square API
- `GET /completed-orders` - List order IDs marked as completed
- `POST /completed-orders` - Post an ID of an order marked completed
- `DELETE /completed-orders/{order_id}` - Delete a completed order ID



## Data Models

### Recipe
```python
{
    "id": integer,
    "label": string,
    "category_id": integer,
    "ingredient_amounts": [
        {
            "size": string,
            "ingredient": {
                "id": integer,
                "label": string
            },
            "amount": string
        }
    ],
    "steps": string,
    "notes": string,
    "image_url": string,
    "creator_id": string,
    "created_date": datetime
}
```

### Category
```python
{
    "id": integer,
    "label": string
}
```

### Ingredient
```python
{
    "id": integer,
    "label": string
}
```

### Code Style
This project uses:
- autopep8 for code formatting
- pylint for code linting
- pylint-django for Django-specific linting

## CORS Configuration

The API is configured to accept requests from:
- http://localhost:3000
- http://127.0.0.1:3000
- http://localhost:5173
- http://127.0.0.1:5173

## Authentication

The API is currently only designed to work with a client using Google Firebase for authentication.

## Acknowledgments

- Built with Django REST Framework
- CORS handling by django-cors-headers
- Authentication by Django REST Framework TokenAuthentication

## Contributors
- Mike McGee
