from rest_framework import serializers

from accounts.serializers import UserSerializer
from billing.models import BillingProfile


class BillingProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BillingProfile
        fields = ['id', 'user', 'email']
