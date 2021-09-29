from django.urls import path

from shopping.views.shopping_item import ShoppingItemListView, ShoppingItemCreateView, ShoppingItemUpdateView
from shopping.views.types import TypeUrgencyListView

app_name = 'shopping'

urlpatterns = [
    path('list', ShoppingItemListView.as_view(), name='list'),
    path('create', ShoppingItemCreateView.as_view(), name='create'),
    path('update/<str:pk>', ShoppingItemUpdateView.as_view(), name='update'),
    path('urgencies/list', TypeUrgencyListView.as_view(), name='urgencies_list'),

]
