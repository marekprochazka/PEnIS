from rest_framework import serializers

from shopping.models import ShoppingItem


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ['description', 'quantity', 'urgency', 'bought']
