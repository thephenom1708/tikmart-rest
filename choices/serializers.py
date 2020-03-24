from rest_framework import serializers

from .models import Color, ClothingCategory, ClothingOccasion, ClothingSize, AutomobileType, Sport, Author, Publisher, \
    Language, BookGenre
from .models import FootwearSize, FootwearCategory


class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = [
			'id', 'name', 'hexcode'
		]


class FootwearSizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = FootwearSize
		fields = [
			'id', 'uk_in', 'eu', 'length'
		]


class FootwearCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = FootwearCategory
		fields = [
			'id', 'name'
		]


class ClothingCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ClothingCategory
		fields = [
			'id', 'name', 'gender'
		]


class ClothingOccasionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClothingOccasion
		fields = [
			'id', 'name'
		]


class ClothingSizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClothingSize
		fields = [
			'id', 'value', 'chest', 'shoulder', 'length', 'type'
		]


class AutomobileTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = AutomobileType
		fields = [
			'id', 'name'
		]


class SportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sport
		fields = [
			'id', 'name'
		]


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = [
			'id', 'first_name', 'last_name', 'email'
		]


class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = [
			'id', 'name', 'city', 'country', 'website'
		]


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = [
			'id', 'name'
		]


class BookGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookGenre
		fields = [
			'id', 'name'
		]
