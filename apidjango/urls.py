from django.urls import path, re_path
from appsauth import views

urlpatterns = [
    re_path('login',views.login),
    re_path('signup',views.signup),
    re_path('test-token',views.test_token),
]
