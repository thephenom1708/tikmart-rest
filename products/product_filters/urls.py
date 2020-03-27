from django.conf.urls import url
from products.product_filters.views import ProductFiltersRetrieveAPI

app_name = 'product_filters_api'

urlpatterns = [
    url(r'^(?P<product_type>[0-9a-z-]+)/$', ProductFiltersRetrieveAPI.as_view(), name='product-filters-api')
]
