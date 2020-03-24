from django.conf.urls import url, include

app_name = 'api'

urlpatterns = [
    url(r'^auth/', include('accounts.urls', namespace='accounts_api')),
    url(r'^products/(?P<product_type>[0-9a-z]+)/', include('products.urls', namespace='products_api')),
    url(r'^filters/', include('products.urls', namespace='filters_api')),
    url(r'^products/reviews/', include('reviews.urls', namespace='reviews_api')),
    url(r'^wishlist/', include('wishlist.urls', namespace='wishlist_api')),
    # url(r'^productDetails/', include('products.urls', namespace='product_details_api')),
    url(r'^orders/', include('orders.urls', namespace='orders_api')),
    url(r'^addresses/', include('addresses.urls', namespace='addresses_api')),
]