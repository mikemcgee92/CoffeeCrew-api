from datetime import datetime
from coffeecrewapi.models import Recipe, Category, Ingredient, IngredientAmount
from .ingredient_amount import IngredientAmountSerializer
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class RecipeSerializer(serializers.ModelSerializer):
  """JSON serializer for recipes"""
    
  ingredient_amounts = IngredientAmountSerializer(many=True, read_only=True)
  class Meta:
    model = Recipe
    fields = (
      "id",
      "label",
      "category_id",
      "ingredient_amounts",
      "steps",
      "notes",
      "image_url",
      "creator_id",
      "created_date",
    )
    depth = 2

class Recipes(ViewSet):
  """Request handlers for Recipes in the CoffeeCrew app"""
  
  permission_classes = (AllowAny,)
  
  def list(self, request):
    """Returns a list of all recipe objects following a successful GET request to /recipes"""
    
    recipes = Recipe.objects.all()
    
    # support filtering by category and creator id
    category_id = self.request.query_params.get("category_id", None)
    creator_id = self.request.query_params.get("creator_id", None)
    
    if category_id is not None:
      recipes = recipes.filter(category_id = category_id)
    
    if creator_id is not None:
      recipes = recipes.filter(creator_id = creator_id)
    
    serializer = RecipeSerializer(
      recipes, many=True, context={"request": request}
    )
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    """Returns a single recipe object instance following a successful GET request to /recipes/[id]"""
    
    try:
      recipe = Recipe.objects.get(pk=pk)
      
      serializer = RecipeSerializer(recipe, context={"request": request})
      return Response(serializer.data)
    except Recipe.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def create(self, request):
    """Create a recipe object
    
    Returns status code 201 - created on success
    """
    
    new_recipe = Recipe()
    new_recipe.label = request.data["label"]
    new_recipe.category_id = Category.objects.get(id=request.data["category_id"])
    new_recipe.steps = request.data["steps"]
    new_recipe.notes = request.data["notes"]
    new_recipe.image_url = request.data["image_url"]
    new_recipe.creator_id = request.data["creator_id"]
    new_recipe.created_date = datetime.now()
    
    new_recipe.save()
    
    serializer = RecipeSerializer(
      new_recipe, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk=None):
    """Update a recipe object
    
    Returns status code 204 - no content on success"""
    
    recipe = Recipe.objects.get(pk=pk)
    recipe.label = request.data["label"]
    recipe.category_id = Category.objects.get(id=request.data["category_id"])
    recipe.steps = request.data["steps"]
    recipe.notes = request.data["notes"]
    recipe.image_url = request.data["image_url"]
    recipe.creator_id = request.data["creator_id"]
    recipe.created_date = datetime.now()
    
    recipe.save()
    
    return Response({}, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk=None):
    """Delete a recipe object
    
    Returns status code 204 - no content on success"""
    
    try:
      recipe = Recipe.objects.get(pk=pk)
      recipe.delete()
      
      return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Recipe.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  @action(methods=["post", "delete"], detail=True, url_path="ingredient")
  def ingredients(self, request, pk=None):
    """Add or remove an ingredient to/from a recipe"""
    
    if request.method == "POST":
      ingredient_amount = IngredientAmount()
      
      ingredient_amount.recipe = Recipe.objects.get(pk=pk)
      ingredient_amount.size = request.data["size"]
      ingredient_amount.ingredient = Ingredient.objects.get(id=request.data["ingredient"])
      ingredient_amount.amount = request.data["amount"]
      
      ingredient_amount.save()
      
      return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == "DELETE":
      ingredient = Ingredient.objects.get(id=request.data["ingredient"])
      recipe = Recipe.objects.get(pk=pk)
      size = request.data["size"]
      amount = request.data["amount"]
      
      ingredient_amount = IngredientAmount.objects.get(recipe=recipe, size=size, ingredient=ingredient, amount=amount)
      ingredient_amount.delete()
      
      return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
  
  @action(methods=["delete"], detail=True, url_path="remove-ingredients")
  def remove_ingredients(self, request, pk=None):
    """Remove all ingredients from a recipe"""
    
    if request.method == "DELETE":
      recipe = Recipe.objects.get(pk=pk)
      ingredient_amounts = IngredientAmount.objects.filter(recipe=recipe)
      ingredient_amounts.delete()
      
      return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
