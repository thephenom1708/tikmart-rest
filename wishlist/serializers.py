from rest_framework import serializers

from accounts.serializers import UserSerializer
from products.serializers import ProductSerializer
from wishlist.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Wishlist
        fields = '__all__'

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #
    #     wishlist_obj, wishlist_created = Wishlist.objects.new_or_get(request=request)
    #     return wishlist_obj
