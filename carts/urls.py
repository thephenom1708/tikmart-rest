from django.conf.urls import url

from .views import (
        cart_home,
        update_cart_quantity,
        delete_product_in_cart,
        cart_update, 
        checkout_home,
        set_payment_method,
        checkout_done_view
        )

app_name = 'cart'

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^set_payment_method/$', set_payment_method, name='payment_method'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
    url(r'^updateQuantity/(?P<cart_id>[0-9a-z]+)/(?P<product_id>[0-9a-z]+)/$', update_cart_quantity,
        name='update_cart_quantity'),
    url(r'^delete_from_cart/(?P<cart_id>[0-9a-z]+)/(?P<product_id>[0-9a-z]+)/$', delete_product_in_cart,
        name='delete_product_in_cart')
]

