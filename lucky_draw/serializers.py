from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserSerializer
from lucky_draw.models import LuckyDraw, LuckyDrawProfile


class LuckyDrawSerializer(ModelSerializer):
    users = UserSerializer(many=True)
    winner = UserSerializer()

    class Meta:
        model = LuckyDraw
        fields = ['id', 'users', 'winner']


class LuckyDrawProfileSerializer(ModelSerializer):
    class Meta:
        model = LuckyDrawProfile
        fields = '__all__'
