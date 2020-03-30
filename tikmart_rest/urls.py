from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from tikmart_rest import api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    # url(r'^', include('ui.urls', namespace='ui')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
]

admin.site.site_header = "Tikmart Administration"
admin.site.site_title = "Tikmart Admin Portal"
admin.site.index_title = "Welcome to Tikmart Admin Portal"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
