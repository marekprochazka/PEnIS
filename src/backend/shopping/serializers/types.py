from rest_framework import serializers

from shopping.models.types import TypeUrgency


class TypeUrgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUrgency
        fields = ['identifier', 'description']
