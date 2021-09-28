from rest_framework import serializers

from sleepover_form.models import SleepoverRequest
from sleepover_form.serializers.types import TypeCoitusProbabilitySerializer
from django.conf import settings


class SleepoverRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepoverRequest
        fields = ['requester_name', 'sleepover_date_from', 'sleepover_date_to',
                  'estimated_arrive_time', 'estimated_leave_time',
                  'num_persons', 'accepted', 'coitus',
                  'estimated_coitus_time_start', 'estimated_coitus_time_end', 'coitus_probability',
                  'note'
                  ]


class SleepoverRequestSerializer(SleepoverRequestUpdateSerializer):
    coitus_probability = TypeCoitusProbabilitySerializer()


class SleepoverRequestListSerializer(serializers.ModelSerializer):
    coitus_probability = TypeCoitusProbabilitySerializer()

    class Meta:
        model = SleepoverRequest
        fields = ['id', 'requester_name', 'sleepover_date_from', 'sleepover_date_to',
                  'num_persons', 'accepted', 'coitus', 'coitus_probability'
                  ]


class SleepoverRequestCalendarListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()

    def get_name(self, instance):
        return f'{instance.requester_name} {f"- {instance.note}" if instance.note else ""}'

    def get_start(self, instance):
        date_string = instance.sleepover_date_from.strftime('%Y-%m-%d')
        if instance.estimated_arrive_time:
            time_string = instance.estimated_arrive_time.strftime('%H:%M')
            return f'{date_string} {time_string}'
        return date_string

    def get_end(self, instance):
        date_string = instance.sleepover_date_to.strftime('%Y-%m-%d')
        if instance.estimated_leave_time:
            time_string = instance.estimated_leave_time.strftime('%H:%M')
            return f'{date_string} {time_string}'
        return date_string

    def get_color(self, instance):
        if instance.coitus:
            return settings.COITUS_COLORS[instance.coitus_probability.identifier]
        return settings.COITUS_COLORS['default']

    class Meta:
        model = SleepoverRequest
        fields = ['id', 'name', 'start', 'end', 'color']
