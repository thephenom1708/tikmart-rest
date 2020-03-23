from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from categories.filters import (
    FootwearFilter,
    ClothingFilter,
    AutomobileFilter,
    FurnitureFilter,
    SportsEquipmentFilter,
    BookFilter
)

from categories.models import (
    Footware,
    Clothing,
    Automobile,
    Furniture,
    SportsEquipment,
    Book
)

from categories.serializers import (
    FootwearSerializer,
    ClothingSerializer,
    AutomobileSerializer,
    FurnitureSerializer,
    SportsEquipmentSerializer,
    BookSerializer
)


class FootwearViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = FootwearSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = FootwearFilter
    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']

    search_fields = ['title', 'brand', 'type__name']

    queryset = Footware.objects.filter(active=True)


class ClothingViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = ClothingSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ClothingFilter

    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']
    search_fields = ['title', 'brand', 'type', 'sleeve', 'category__name', 'occasion__name']

    queryset = Clothing.objects.filter(active=True)


class AutomobileViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = AutomobileSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = AutomobileFilter

    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']
    search_fields = ['title', 'brand', 'type__name']

    queryset = Automobile.objects.filter(active=True)


class FurnitureViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = FurnitureSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = FurnitureFilter

    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']
    search_fields = ['title', 'brand', 'material']

    queryset = Furniture.objects.filter(active=True)


class SportsEquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = SportsEquipmentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = SportsEquipmentFilter

    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']
    search_fields = ['title', 'brand', 'related_sport__name', 'material']

    queryset = SportsEquipment.objects.filter(active=True)


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = BookFilter

    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']
    search_fields = ['title', 'brand', 'author__first_name', 'author__last_name', 'language__name', 'publisher__name',
                     'genere__name']

    queryset = Book.objects.filter(active=True)
