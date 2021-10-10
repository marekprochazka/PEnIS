from django.contrib import admin

# Register your models here.
from shopping.models import ShoppingItem
from shopping.models.types import TypeUrgency
from shopping.models import CashDue


class ShoppingListAdmin(admin.ModelAdmin):
    pass


class TypeUrgencyAdmin(admin.ModelAdmin):
    pass


class CashDueAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShoppingItem, ShoppingListAdmin)
admin.site.register(TypeUrgency, TypeUrgencyAdmin)
admin.site.register(CashDue, CashDueAdmin)
