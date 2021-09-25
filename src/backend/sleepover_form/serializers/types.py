from rest_framework import serializers

from sleepover_form.models import TypeCoitusProbability


class TypeCoitusProbabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCoitusProbability
        fields = ['identifier', 'description', 'id']
