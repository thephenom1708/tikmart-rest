from rest_framework import serializers

from accounts.serializers import UserSerializer
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class PostReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        user = self.context.get('request').user
        product = validated_data.get('product')
        rating = validated_data.get('rating')
        content = validated_data.get('content')

        review = Review.objects.create(user=user, product=product, rating=rating, content=content)
        return review



