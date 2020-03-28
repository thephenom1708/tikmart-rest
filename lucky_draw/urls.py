from django.conf.urls import url

from lucky_draw.views import LuckyDrawAPI, LuckyDrawProfileAPI

app_name = 'lucky_draw_api'

urlpatterns = [
    url(r'^profile/(?P<lucky_draw_id>[0-9a-z]+)/$', LuckyDrawProfileAPI.as_view(), name='lucky-draw-profile-api'),
    url(r'^', LuckyDrawAPI.as_view(), name='lucky-draw-api'),
]
