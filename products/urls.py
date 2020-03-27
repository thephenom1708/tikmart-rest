from django.conf.urls import url, include
from rest_framework import routers

from products.product_filters.views import ProductFiltersRetrieveAPI
from products.views import ProductViewSet, ProductDetailViewSet

app_name = 'products_api'

router = routers.SimpleRouter()
router.register('details', ProductDetailViewSet, 'product-detail-api')
router.register(r'(?P<product_type>[0-9a-z-]+)', ProductViewSet, 'products-api')

urlpatterns = [
    url(r'filters/', include('products.product_filters.urls', namespace='product_filters_api'))
]

urlpatterns += router.urls
