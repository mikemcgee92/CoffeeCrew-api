from coffeecrewapi.models import UserInfo
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class UserInfoSerializer(serializers.ModelSerializer):
  """JSON serializer for user info"""
  
  class Meta:
    model = UserInfo
    fields = (
      "firebase_key",
      "display_name",
      "is_manager",
    )

class UserInfos(ViewSet):
  """Request handlers for UserInfo objects"""
  
  permission_classes = (AllowAny, )
  
  def list(self, request):
    """Returns a list of all user's info"""
    
    user_infos = UserInfo.objects.all()
    
    serializer = UserInfoSerializer(
      user_infos, many=True, context={"request": request}
    )
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    """Returns a single user info object following a successful GET request to /user-info/[firebase_key]"""
    
    try:
      user_info = UserInfo.objects.get(firebase_key=pk)
      
      serializer = UserInfoSerializer(user_info, context={"request": request})
      return Response(serializer.data)
    except UserInfo.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def create(self, request):
    """Create a user info object following a successful POST request to /user-info, with valid JSON in the request body matching the UserInfo model"""
    
    new_user_info = UserInfo()
    new_user_info.firebase_key = request.headers.get('Authorization')
    new_user_info.display_name = request.data["display_name"]
    new_user_info.is_manager = False
    
    new_user_info.save()
    
    serializer = UserInfoSerializer(
      new_user_info, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk=None):
    """Update a user info object matching the request firebase_key following a successful PUT request to user-info/[firebase_key] with valid JSON in the request body matching the UserInfo model"""
    
    user_info = UserInfo.objects.get(firebase_key=pk)
    user_info.display_name = request.data["display_name"]
    user_info.is_manager = request.data["is_manager"]

    user_info.save()
    
    return Response({}, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk=None):
    """Delete a user info object matching the requested firebase_key following a successful DELETE request to user-info/[firebase_key]"""
    
    try:
      user_info = UserInfo.objects.get(firebase_key=pk)
      user_info.delete()
    except UserInfo.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
