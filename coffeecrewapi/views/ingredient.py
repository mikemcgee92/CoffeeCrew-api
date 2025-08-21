from coffeecrewapi.models import Ingredient
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class IngredientSerializer(serializers.ModelSerializer):
  """JSON serializer for ingredients"""
  
  class Meta:
    model = Ingredient
    fields = (
      "id",
      "label",
    )

class Ingredients(ViewSet):
  """Request handlers for Ingredients in the CoffeeCrew app"""
  
  permission_classes = (IsAuthenticatedOrReadOnly,)
  
  def list(self, request):
    """Returns a list of all ingredient objects following a successful GET request to /ingredients"""
    
    ingredients = Ingredient.objects.all()
    
    serializer = IngredientSerializer(
      ingredients, many=True, context={"request": request}
    )
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    """Returns a single ingredient object instance following a successful GET request to /ingredients/[id]"""

    try:
      ingredient = Ingredient.objects.get(pk=pk)
      
      serializer = IngredientSerializer(ingredient, context={"request": request})
      return Response(serializer.data)
    except Ingredient.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
