from django.conf.urls import url

from carts.views import CartAPI, CartProductAPI

app_name = 'carts_api'

urlpatterns = [
    url(r'^cart-product/(?P<id>[0-9a-z]+)/$', CartProductAPI.as_view(), name='cart-product-api'),
    url(r'^', CartAPI.as_view(), name='cart-api')
]
