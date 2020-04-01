from .views import RegisterAPI, LoginAPI, UserAPI, ChangePasswordAPI
from knox import views as knox_views

from django.conf.urls import url

app_name = 'accounts_api'

urlpatterns = [
  url(r'^register/$', RegisterAPI.as_view(), name='register-api'),
  url(r'^login/$', LoginAPI.as_view(), name='login-api'),
  url(r'^user/$', UserAPI.as_view(), name='user-api'),
  url(r'^logout/$', knox_views.LogoutView.as_view(), name='logout-api'),
  url(r'^change-password/$', ChangePasswordAPI.as_view(), name='change-password-api'),
]