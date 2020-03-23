from rest_framework import serializers

from categories.models import Footware, Clothing, Automobile, Furniture, SportsEquipment


class FootwearBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footware
        fields = ['brand']


class ClothingBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['brand']


class ClothingSleeveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['sleeve']


class AutomobileBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automobile
        fields = ['brand']


class FurnitureBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['brand']


class SportsEquipmentBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsEquipment
        fields = ['brand']
