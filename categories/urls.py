from rest_framework import routers

from categories.views import (
    FootwearViewSet,
    ClothingViewSet,
    AutomobileViewSet,
    FurnitureViewSet,
    SportsEquipmentViewSet,
    BookViewSet
)

app_name = 'categories_api'

router = routers.DefaultRouter()
router.register('footwear', FootwearViewSet, 'footwear_api')
router.register('clothing', ClothingViewSet, 'clothing_api')
router.register('automobile', AutomobileViewSet, 'automobile_api')
router.register('furniture', FurnitureViewSet, 'furniture_api')
router.register('sportsequipment', SportsEquipmentViewSet, 'sports_equipment_api')
router.register('book', BookViewSet, 'book_api')

urlpatterns = router.urls
