from django.db import models
from datetime import date
from django.db.models import Q


class SleepoverRequestManager(models.Manager):
    def get_list_without_past_requests(self):
        today = date.today()
        return super().get_queryset().filter(
            Q(sleepover_date_to__range=[today, '3000-01-01']) | Q(sleepover_date_to__isnull=True))
