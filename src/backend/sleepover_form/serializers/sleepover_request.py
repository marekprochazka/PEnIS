from rest_framework import serializers

from sleepover_form.models import SleepoverRequest


class SleepoverRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepoverRequest
        fields = ['requester_name', 'sleepover_date_from', 'sleepover_date_to',
                  'estimated_arrive_time', 'estimated_leave_time',
                  'num_persons', 'accepted', 'coitus',
                  'estimated_coitus_time_start', 'estimated_coitus_time_end']


class SleepoverRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepoverRequest
        fields = ['id', 'requester_name', 'sleepover_date_from', 'sleepover_date_to',
                  'num_persons', 'accepted', 'coitus',
                  ]
