from django.conf.urls import url
from rest_framework import routers

from orders.views import OrderViewSet, OrderCreateAPI

app_name = 'orders_api'

router = routers.DefaultRouter()
router.register('', OrderViewSet, 'orders_api')
# router.register('checkout', OrderCheckoutViewSet, 'order_checkout_api')

urlpatterns = [
    url(
        r'^create-order/(?P<billing_profile>[0-9a-z]+)/(?P<cart>[0-9a-z]+)/$',
        OrderCreateAPI.as_view(),
        name='order-create-api'
    )
]

urlpatterns += router.urls
