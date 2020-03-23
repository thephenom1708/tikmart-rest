from django.conf.urls import url
from .views import (
    FootwearFiltersAPIView,
    ClothingFiltersAPIView,
    AutomobileFiltersAPIView,
    FurnitureFiltersAPIView,
    SportsEquipmentFiltersAPIView,
    BookFiltersAPIView
)

app_name = 'categories_filters_api'

urlpatterns = [
    url(r'^footwear/$', FootwearFiltersAPIView.as_view(), name='footwear-filters-api'),
    url(r'^clothing/$', ClothingFiltersAPIView.as_view(), name='clothing-filters-api'),
    url(r'^automobile/$', AutomobileFiltersAPIView.as_view(), name='automobile-filters-api'),
    url(r'^furniture/$', FurnitureFiltersAPIView.as_view(), name='furniture-filters-api'),
    url(r'^sportsequipment/$', SportsEquipmentFiltersAPIView.as_view(), name='sports-equipment-filters-api'),
    url(r'^book/$', BookFiltersAPIView.as_view(), name='book-filters-api'),
]
