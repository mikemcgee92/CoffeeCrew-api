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
            "completed_order",
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
    
    def retrieve(self, request, pk=None):
        """Returns a single completed order object"""
        
        try:
            completed_order = CompletedOrder.objects.get(pk=pk)
            
            serializer = CompletedOrderSerializer(completed_order, context={"request": request})
            return Response(serializer.data)
        except CompletedOrder.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    