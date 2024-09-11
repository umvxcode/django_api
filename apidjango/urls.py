from django.urls import path, re_path
from appsauth.views import views_auth

urlpatterns = [
    re_path('login',views_auth.login),
    re_path('umen',views_auth.ulogin),
    re_path('signup',views_auth.signup),
    re_path('test-token',views_auth.test_token),
]
