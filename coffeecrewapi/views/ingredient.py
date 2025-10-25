from coffeecrewapi.models import Ingredient
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.db.models.functions import Lower


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
  
  permission_classes = (AllowAny,)
  
  def list(self, request):
    """Returns a list of all ingredient objects following a successful GET request to /ingredients"""
    
    ingredients = Ingredient.objects.order_by(Lower('label'))
    
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

  def create(self, request):
    """Creates a new ingredient object following a successful POST request to /ingredients"""
    
    new_ingredient = Ingredient()
    new_ingredient.label = request.data["label"]
    new_ingredient.creator_id = request.headers.get("Authorization")
    
    new_ingredient.save()
    
    serializer = IngredientSerializer(
      new_ingredient, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk=None):
    """Update a ingredient object matching the requested id following a successful PUT request to ingredients/[id] with valid JSON in the request body matching the ingredient model"""
    
    ingredient = Ingredient.objects.get(pk=pk)
    ingredient.label = request.data["label"]
    ingredient.creator_id = request.headers.get('Authorization')
    
    ingredient.save()
    
    return Response({}, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk=None):
    """Delete a ingredient object mathing the requested id following a successful DELETE request to ingredients/[id]"""
    
    try:
      ingredient = Ingredient.objects.get(pk=pk)
      if request.headers.get('Authorization') != ingredient.creator_id:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)
      ingredient.delete()
      
      return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Ingredient.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
