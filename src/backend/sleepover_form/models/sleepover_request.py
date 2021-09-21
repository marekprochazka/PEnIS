from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class SleepoverRequest(BaseModel):
    requester_name = models.CharField(max_length=64, verbose_name=_('Requester name'), null=True, blank=True)
    sleepover_date_from = models.DateField(verbose_name=_('Sleepover date from'), null=True, blank=True)
    sleepover_date_to = models.DateField(verbose_name=_('Sleepover date to'), null=True, blank=True)
    estimated_arrive_time = models.TimeField(null=True, blank=True, verbose_name=_('Estimated arrive time'))
    estimated_leave_time = models.TimeField(null=True, blank=True, verbose_name=_('Estimated leave time'))
    num_persons = models.CharField(max_length=4, verbose_name=_('Number of persons'), null=True, blank=True)
    accepted = models.BooleanField(default=False, verbose_name=_('Accepted'))

    coitus = models.BooleanField(verbose_name=_('Is coitus'), default=False)
    estimated_coitus_time_start = models.TimeField(null=True, blank=True, verbose_name=_('Estimated coitus time start'))
    estimated_coitus_time_end = models.TimeField(null=True, blank=True, verbose_name=_('Estimated coitus time start'))
