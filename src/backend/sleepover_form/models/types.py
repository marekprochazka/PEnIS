from core.models import BaseTypeModel
from django.utils.translation import gettext_lazy as _
from django.db import models


class TypeCoitusProbability(BaseTypeModel):
    description_alt = models.CharField(verbose_name=_("Alternative description"), max_length=255)

    class Meta:
        verbose_name = _('Type coitus probability')
        verbose_name_plural = _('Type coitus probabilities')
        ordering = ['-order']



