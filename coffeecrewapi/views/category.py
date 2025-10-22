from coffeecrewapi.models import Category
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from coffeecrewapi.middleware import cors_allow_all


class CategorySerializer(serializers.ModelSerializer):
  """JSON serializer for categories"""
  
  class Meta:
    model = Category
    fields = (
      "id",
      "label",
      "creator_id",
    )

class Categories(ViewSet):
  """Request handlers for Categories in the CoffeeCrew app"""
  
  permission_classes = (AllowAny,)
  
  @cors_allow_all
  def list(self, request):
    """Returns a list of all category objects following a successful GET request to /categories"""
    
    categories = Category.objects.all()
    
    serializer = CategorySerializer(
      categories, many=True, context={"request": request}
    )
    return Response(serializer.data)
  
  @cors_allow_all
  def retrieve(self, request, pk=None):
    """Returns a single category object instance following a successful GET request to /categories/[id]"""
    
    try:
      category = Category.objects.get(pk=pk)
      
      serializer = CategorySerializer(category, context={"request": request})
      return Response(serializer.data)
    except Category.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  @cors_allow_all
  def create(self, request):
    """Create a category object following a successful POST request to /categories, with valid JSON in the request body matching the category model"""
    
    new_category = Category()
    new_category.label = request.data["label"]
    new_category.creator_id = request.headers.get('Authorization')
    
    new_category.save()
    
    serializer = CategorySerializer(
      new_category, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  @cors_allow_all
  def update(self, request, pk=None):
    """Update a category object matching the requested id following a successful PUT request to categories/[id] with valid JSON in the request body matching the category model"""
    
    category = Category.objects.get(pk=pk)
    category.label = request.data["label"]
    category.creator_id = request.headers.get('Authorization')
    
    category.save()
    
    return Response({}, status=status.HTTP_204_NO_CONTENT)
  
  @cors_allow_all
  def destroy(self, request, pk=None):
    """Delete a category object mathing the requested id following a successful DELETE request to categories/[id]"""
    
    try:
      category = Category.objects.get(pk=pk)
      if request.headers.get('Authorization') != category.creator_id:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)
      category.delete()
      
      return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
