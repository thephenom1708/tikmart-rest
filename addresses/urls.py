from rest_framework import routers

from addresses.views import AddressViewSet

app_name = 'addresses_api'

router = routers.DefaultRouter()
router.register('', AddressViewSet, basename='addresses_api')

urlpatterns = router.urls
