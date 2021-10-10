from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class CashDue(BaseModel):
    description = models.CharField(max_length=128, verbose_name=_('Description'))
    user = models.CharField(max_length=128, verbose_name=_('User'))
    money_amount = models.IntegerField(verbose_name=_('Money amount'))
    paid_back = models.BooleanField(default=False, verbose_name=_('Paid back'))

    class Meta:
        verbose_name = _("Cash Due")
        verbose_name_plural = _("Cash Dues")