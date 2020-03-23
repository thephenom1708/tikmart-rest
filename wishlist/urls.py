from rest_framework import routers

from wishlist.views import WishlistViewSet

app_name = 'wishlist_api'

router = routers.DefaultRouter()
router.register('', WishlistViewSet, 'wishlist-api')

urlpatterns = router.urls
