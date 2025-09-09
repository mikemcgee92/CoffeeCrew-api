from coffeecrewapi.models import CompletedOrder
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CompletedOrderSerializer(serializers.ModelSerializer):
    """JSON serializer for completed orders from Square API"""
    
    class Meta:
        model = CompletedOrder
        fields = (
            "order_id",
        )

class CompletedOrders(ViewSet):
    """Request handlers for completed orders from Square API"""
    
    permission_classes = (AllowAny,)
    
    def list(self, request):
        """Returns array of completed order objects"""
        
        completed_orders = CompletedOrder.objects.all()
        
        serializer = CompletedOrderSerializer(
            completed_orders, many=True, context={"request": request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, order_id=None):
        """Returns a single completed order object"""
        
        try:
            completed_order = CompletedOrder.objects.get(order_id=order_id)
            
            serializer = CompletedOrderSerializer(completed_order, context={"request": request})
            return Response(serializer.data)
        except CompletedOrder.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def create(self, request):
        """Create a completed order object following successful POST request to /completeorder"""
        
        new_completed_order = CompletedOrder()
        new_completed_order.order_id = request.data["order_id"]
        
        new_completed_order.save()
        
        serializer = CompletedOrderSerializer(
            new_completed_order, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, order_id=None):
        """Delete a completed order"""
        
        try:
            completed_order = CompletedOrder.objects.get(order_id=order_id)
            completed_order.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except CompletedOrder.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
