from django.urls import path

from shopping.views.shopping_item import ShoppingItemListView

app_name = 'shopping'

urlpatterns = [
    path('list', ShoppingItemListView.as_view(), name='list'),

]
