from django.contrib import admin

# Register your models here.
from shopping.models import ShoppingItem
from shopping.models.types import TypeUrgency


class ShoppingListAdmin(admin.ModelAdmin):
    pass


class TypeUrgencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShoppingItem, ShoppingListAdmin)
admin.site.register(TypeUrgency, TypeUrgencyAdmin)
