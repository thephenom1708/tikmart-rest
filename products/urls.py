from django.conf.urls import url
from rest_framework import routers

from products.product_filters.views import ProductFiltersRetrieveAPI
from products.views import ProductViewSet

app_name = 'products_api'

router = routers.DefaultRouter()
router.register('', ProductViewSet, 'products-api')

urlpatterns = [
    url(
        r'^(?P<product_type>[0-9a-z-]+)/$',
        ProductFiltersRetrieveAPI.as_view(),
        name='product-product_filters-retrieve-api'
    )
]

urlpatterns += router.urls
