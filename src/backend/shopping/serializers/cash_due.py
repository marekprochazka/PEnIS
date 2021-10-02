from rest_framework import serializers

from shopping.models import CashDue


class CashDueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashDue
        fields = ['description', 'user', 'money_amount']


class CashDueUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashDue
        fields = ['paid_back']


class CashDueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashDue
        fields = ['id', 'description', 'user', 'money_amount', 'paid_back']
