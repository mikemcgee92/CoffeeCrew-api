from coffeecrewapi.models import IngredientAmount, Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for ingredients"""
    class Meta:
        model = Ingredient
        fields = ('id', 'label')


class IngredientAmountSerializer(serializers.ModelSerializer):
    """JSON serializer for IngredientAmount join objects between Recipe and Ingredient Objects"""
    
    ingredient = IngredientSerializer(read_only=True)
    
    class Meta:
        model = IngredientAmount
        fields = (
            "size",
            "ingredient",
            "amount"
        )
