from django.contrib import admin

# Register your models here.
from sleepover_form.models import SleepoverRequest


class SleepoverRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(SleepoverRequest, SleepoverRequestAdmin)
