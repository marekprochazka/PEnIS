from rest_framework import serializers

from shopping.models import ShoppingItem
from shopping.serializers.types import TypeUrgencySerializer


class ShoppingItemSerializer(serializers.ModelSerializer):
    urgency = TypeUrgencySerializer()

    class Meta:
        model = ShoppingItem
        fields = ['id', 'description', 'quantity', 'urgency', 'bought']
