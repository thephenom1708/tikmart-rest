from django.conf.urls import url, include

app_name = 'api'

urlpatterns = [
    url(r'^auth/', include('accounts.urls', namespace='accounts_api')),
    # url(r'^filters/', include('products.product_filters.urls', namespace='product_filters_api')),
    url(r'^products/reviews/', include('reviews.urls', namespace='reviews_api')),
    url(r'^products/', include('products.urls', namespace='products_api')),
    url(r'^tags/', include('tags.urls', namespace='tags_api')),
    url(r'^wishlist/', include('wishlist.urls', namespace='wishlist_api')),
    url(r'^cart/', include('carts.urls', namespace='carts_api')),
    url(r'^orders/', include('orders.urls', namespace='orders_api')),
    url(r'^addresses/', include('addresses.urls', namespace='addresses_api')),
    url(r'^lucky-draw/', include('lucky_draw.urls', namespace='lucky_draw_api'))
]
