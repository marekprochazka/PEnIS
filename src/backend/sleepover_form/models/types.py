from core.models import BaseTypeModel
from django.utils.translation import gettext_lazy as _


class TypeCoitusProbability(BaseTypeModel):
    class Meta:
        verbose_name = _('Type coitus probability')
        verbose_name_plural = _('Type coitus probabilities')
        ordering = ['-order']
