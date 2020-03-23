from rest_framework import routers

from reviews.views import ReviewViewSet

app_name = 'reviews_api'

router = routers.DefaultRouter()
router.register('', ReviewViewSet, 'reviews-api')

urlpatterns = router.urls
