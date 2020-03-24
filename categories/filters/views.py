from drf_multiple_model.views import ObjectMultipleModelAPIView

from categories.filters.serializers import (
    FootwearBrandSerializer,
    ClothingBrandSerializer, ClothingSleeveSerializer,
    AutomobileBrandSerializer,
    FurnitureBrandSerializer,
    SportsEquipmentBrandSerializer,
)
from categories.models import (
    Footware, Clothing, Automobile, Furniture, SportsEquipment
)
from choices.models import (
    Color, FootwearSize, FootwearCategory,
    ClothingSize, ClothingCategory, ClothingOccasion,
    AutomobileType,
    Sport,
    Language, BookGenre
)
from choices.serializers import (
    ColorSerializer,
    FootwearSizeSerializer, FootwearCategorySerializer,
    ClothingCategorySerializer, ClothingSizeSerializer, ClothingOccasionSerializer,
    AutomobileTypeSerializer,
    SportSerializer,
    BookGenreSerializer, LanguageSerializer
)


class FootwearFiltersAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Color.objects.all(),
            'serializer_class': ColorSerializer,
            'label': 'colors'
        },
        {
            'queryset': FootwearCategory.objects.all(),
            'serializer_class': FootwearCategorySerializer,
            'label': 'categories',
        },
        {
            'queryset': Footware.objects.values('brand').distinct(),
            'serializer_class': FootwearBrandSerializer,
            'label': 'brands'
        },
        {
            'queryset': FootwearSize.objects.all(),
            'serializer_class': FootwearSizeSerializer,
            'label': 'sizes'
        }
    ]


class ClothingFiltersAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Color.objects.all(),
            'serializer_class': ColorSerializer,
            'label': 'colors'
        },
        {
            'queryset': ClothingCategory.objects.all(),
            'serializer_class': ClothingCategorySerializer,
            'label': 'categories',
        },
        {
            'queryset': Clothing.objects.values('brand').distinct(),
            'serializer_class': ClothingBrandSerializer,
            'label': 'brands'
        },
        {
            'queryset': Clothing.objects.values('sleeve').distinct(),
            'serializer_class': ClothingSleeveSerializer,
            'label': 'sleeves'
        },
        {
            'queryset': ClothingSize.objects.all(),
            'serializer_class': ClothingSizeSerializer,
            'label': 'sizes'
        },
        {
            'queryset': ClothingOccasion.objects.all(),
            'serializer_class': ClothingOccasionSerializer,
            'label': 'occasions'
        }
    ]


class AutomobileFiltersAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Color.objects.all(),
            'serializer_class': ColorSerializer,
            'label': 'colors'
        },
        {
            'queryset': AutomobileType.objects.all(),
            'serializer_class': AutomobileTypeSerializer,
            'label': 'categories',
        },
        {
            'queryset': Automobile.objects.values('brand').distinct(),
            'serializer_class': AutomobileBrandSerializer,
            'label': 'brands'
        }
    ]


class FurnitureFiltersAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Color.objects.all(),
            'serializer_class': ColorSerializer,
            'label': 'colors'
        },
        {
            'queryset': Furniture.objects.values('brand').distinct(),
            'serializer_class': FurnitureBrandSerializer,
            'label': 'brands'
        }
    ]


class SportsEquipmentFiltersAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Color.objects.all(),
            'serializer_class': ColorSerializer,
            'label': 'colors'
        },
        {
            'queryset': Sport.objects.all(),
            'serializer_class': SportSerializer,
            'label': 'related_sports',
        },
        {
            'queryset': SportsEquipment.objects.values('brand').distinct(),
            'serializer_class': SportsEquipmentBrandSerializer,
            'label': 'brands'
        }
    ]


class BookFiltersAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {
            'queryset': Language.objects.all(),
            'serializer_class': LanguageSerializer,
            'label': 'languages'
        },
        {
            'queryset': BookGenre.objects.all(),
            'serializer_class': BookGenreSerializer,
            'label': 'genres'
        }
    ]