from django.urls import path

from shopping.views.cash_due import CashDueListView, CashDueCreateView, CashDueUpdateView
from shopping.views.shopping_item import ShoppingItemListView, ShoppingItemCreateView, ShoppingItemUpdateView
from shopping.views.types import TypeUrgencyListView

app_name = 'shopping'

urlpatterns = [
    path('items/list', ShoppingItemListView.as_view(), name='list'),
    path('items/create', ShoppingItemCreateView.as_view(), name='create'),
    path('items/update/<str:pk>', ShoppingItemUpdateView.as_view(), name='update'),
    path('urgencies/list', TypeUrgencyListView.as_view(), name='urgencies_list'),

    path('cash-due/list', CashDueListView.as_view(), name='cash_due_list'),
    path('cash-due/create', CashDueCreateView.as_view(), name='cash_due_create'),
    path('cash-due/update/<str:pk>', CashDueUpdateView.as_view(), name='cash_due_update')

]
