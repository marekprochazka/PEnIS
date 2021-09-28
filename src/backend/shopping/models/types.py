from core.models import BaseTypeModel
from django.utils.translation import gettext_lazy as _


class TypeUrgency(BaseTypeModel):
    class Meta:
        verbose_name = _('Type urgency')
        verbose_name_plural = _('Type urgencies')
        ordering = ['-order']
