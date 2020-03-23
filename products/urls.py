from rest_framework import routers

from products.views import ProductViewSet

app_name = 'product_detail_api'

router = routers.DefaultRouter()
router.register('', ProductViewSet, 'product_detail_api')

urlpatterns = router.urls
