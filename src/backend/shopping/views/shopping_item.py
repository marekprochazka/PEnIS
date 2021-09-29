from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from shopping.models import ShoppingItem
from shopping.serializers.shopping_item import ShoppingItemSerializer, ShoppingItemCreateSerializer, \
    ShoppingItemUpdateSerializer


class ShoppingItemListView(ListAPIView):
    serializer_class = ShoppingItemSerializer

    def get_queryset(self):
        show_bought = self.request.GET.get('bought')
        if show_bought:
            return ShoppingItem.objects.filter(bought=True)
        return ShoppingItem.objects.filter(bought=False)


class ShoppingItemCreateView(CreateAPIView):
    serializer_class = ShoppingItemCreateSerializer


class ShoppingItemUpdateView(UpdateAPIView):
    serializer_class = ShoppingItemUpdateSerializer
    queryset = ShoppingItem.objects.all()
