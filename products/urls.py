from django.conf.urls import url, include
from rest_framework import routers

from products.views import ProductViewSet, ProductDetailViewSet, FeaturedProductsAPI

app_name = 'products_api'

router = routers.SimpleRouter()
router.register('details', ProductDetailViewSet, 'product-detail-api')
router.register(r'(?P<product_type>[0-9a-z-]+)', ProductViewSet, 'products-api')

urlpatterns = [
    url(r'filters/', include('products.product_filters.urls', namespace='product_filters_api')),
    url(r'featured/', FeaturedProductsAPI.as_view(), name='featured-products-api'),
]

urlpatterns += router.urls
