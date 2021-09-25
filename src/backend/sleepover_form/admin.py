from django.contrib import admin

# Register your models here.
from sleepover_form.models import SleepoverRequest, TypeCoitusProbability


class SleepoverRequestAdmin(admin.ModelAdmin):
    pass


class TypeCoitusProbabilityAdmin(admin.ModelAdmin):
    pass


admin.site.register(SleepoverRequest, SleepoverRequestAdmin)
admin.site.register(TypeCoitusProbability, TypeCoitusProbabilityAdmin)
