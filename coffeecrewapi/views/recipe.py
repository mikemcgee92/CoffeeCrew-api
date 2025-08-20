from datetime import datetime
from coffeecrewapi.models import Recipe
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class RecipeSerializer(serializers.ModelSerializer):
  """JSON serializer for recipes"""
  
  class Meta:
    model = Recipe
    fields = (
      "id",
      "label",
      "category_id",
      "steps",
      "notes",
      "image_url",
      "creator_id",
      "created_date",
    )
    depth = 1
    # TODO: Make sure depth is accurate when testing

class Recipes(ViewSet):
  """Request handlers for Recipes in the CoffeeCrew app"""
  
  permission_classes = (IsAuthenticatedOrReadOnly,)
  
  def list(self, request):
    """Returns a list of all recipe objects following a successful GET request to /recipes"""
    
    recipes = Recipe.objects.all()
    
    # support filtering by category
    category_id = self.request.query_params.get("category_id", None)
    
    if category_id is not None:
      recipes = recipes.filter(category_id = category_id)
    
    serializer = RecipeSerializer(
      recipes, many=True, context={"request": request}
    )
    return Response(serializer.data)
  
  def retrieve(sef, request, pk=None):
    """Returns a single recipe object instance following a successful GET request to /recipes/[id]"""
    
    try:
      recipe = Recipe.objects.get(pk=pk)
      
      serializer = RecipeSerializer(recipe, context={"request": request})
      return Response(serializer.data)
    except Recipe.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
