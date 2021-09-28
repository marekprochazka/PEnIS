from rest_framework.generics import ListAPIView

from shopping.models import ShoppingItem
from shopping.serializers.shopping_item import ShoppingItemSerializer


class ShoppingItemListView(ListAPIView):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
