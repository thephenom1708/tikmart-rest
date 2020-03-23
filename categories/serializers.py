from rest_framework import serializers

from choices.serializers import ColorSerializer, ClothingCategorySerializer, ClothingSizeSerializer, \
	ClothingOccasionSerializer, AutomobileTypeSerializer, SportSerializer, BookGenreSerializer, AuthorSerializer, \
	LanguageSerializer, PublisherSerializer
from choices.serializers import FootwearSizeSerializer, FootwearCategorySerializer
from products.reviews import ReviewSerializer

from .models import Footware, Clothing, Automobile, Furniture, SportsEquipment, Book


class FootwearSerializer(serializers.ModelSerializer):
	type = FootwearCategorySerializer(read_only=True)
	sizes = FootwearSizeSerializer(read_only=True, many=True)
	colors = ColorSerializer(read_only=True, many=True)
	reviews = ReviewSerializer(read_only=True, many=True)

	class Meta:
		model = Footware
		fields = [
			'id', 'slug', 'title', 'brand', 'image', 'description', 'type', 'gender',
			'colors', 'sizes',
			'price', 'featured', 'active', 'timestamp',
			'get_absolute_url', 'url', 'reviews'
		]


class ClothingSerializer(serializers.ModelSerializer):
	type = ClothingCategorySerializer(read_only=True)
	occasion = ClothingOccasionSerializer(read_only=True)
	sizes = ClothingSizeSerializer(read_only=True, many=True)
	colors = ColorSerializer(read_only=True, many=True)
	reviews = ReviewSerializer(read_only=True, many=True)

	class Meta:
		model = Clothing
		fields = [
			'id', 'slug', 'title', 'brand', 'image', 'description', 'type', 'gender',
			'category', 'sleeve', 'occasion', 'colors', 'sizes',
			'price', 'featured', 'active', 'timestamp',
			'get_absolute_url', 'url', 'reviews'
		]


class AutomobileSerializer(serializers.ModelSerializer):
	type = AutomobileTypeSerializer(read_only=True)
	colors = ColorSerializer(read_only=True, many=True)
	reviews = ReviewSerializer(read_only=True, many=True)

	class Meta:
		model = Automobile
		fields = [
			'id', 'slug', 'title', 'brand', 'image', 'description',
			'type', 'colors',
			'price', 'featured', 'active', 'timestamp',
			'get_absolute_url', 'url', 'reviews'
		]


class FurnitureSerializer(serializers.ModelSerializer):
	colors = ColorSerializer(read_only=True, many=True)
	reviews = ReviewSerializer(read_only=True, many=True)

	class Meta:
		model = Furniture
		fields = [
			'id', 'slug', 'title', 'brand', 'image', 'description',
			'material', 'colors',
			'price', 'featured', 'active', 'timestamp',
			'get_absolute_url', 'url', 'reviews'
		]


class SportsEquipmentSerializer(serializers.ModelSerializer):
	related_sport = SportSerializer(read_only=True)
	colors = ColorSerializer(read_only=True, many=True)
	reviews = ReviewSerializer(read_only=True, many=True)

	class Meta:
		model = SportsEquipment
		fields = [
			'id', 'slug', 'title', 'brand', 'image', 'description',
			'related_sport', 'weight', 'material', 'colors',
			'price', 'featured', 'active', 'timestamp',
			'get_absolute_url', 'url', 'reviews'
		]


class BookSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True)
	language = LanguageSerializer(read_only=True)
	publisher = PublisherSerializer(read_only=True)
	genre = BookGenreSerializer(read_only=True, many=True)
	reviews = ReviewSerializer(read_only=True, many=True)

	class Meta:
		model = Book
		fields = [
			'id', 'slug', 'title', 'image', 'description',
			'author', 'language', 'publisher', 'genre', 'edition', 'no_of_pages',
			'price', 'featured', 'active', 'timestamp',
			'get_absolute_url', 'url', 'reviews'
		]

