from django.conf.urls import url
from rest_framework import routers

from tags.views import TagViewSet

app_name = 'tags_api'

router = routers.SimpleRouter()
router.register('', TagViewSet, 'tags-api')

# urlpatterns = [
#     url(r'^', TagListAPI.as_view(), name='tags-list-api')
# ]
urlpatterns = router.urls
