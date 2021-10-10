from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _

from shopping.models.types import TypeUrgency


class ShoppingItem(BaseModel):
    description = models.CharField(max_length=128, verbose_name=_('Description'))
    quantity = models.CharField(max_length=128, verbose_name=_('Quantity'))
    urgency = models.ForeignKey(TypeUrgency, on_delete=models.PROTECT, verbose_name=_('Urgency'))
    bought = models.BooleanField(verbose_name=_('Bought'), default=False)
    # TODO Type of product

    class Meta:
        verbose_name = _('Shopping Item')
        verbose_name_plural = _('Shopping Items')