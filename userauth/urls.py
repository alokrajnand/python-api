from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('register/', UserViewSet),
    path('login/', LoginViewSet.as_view()),
    path('email_varification/',
         VarificationViewSet.as_view({'post': 'post_auth'})),
    path('profile/<name>', ProfileViewSet.as_view({'get': 'get_profile'})),
    path('profile/insert/', ProfileViewSet.as_view({'post': 'post_profile'})),
    path('profile/update/<name>',
         ProfileViewSet.as_view({'put': 'put_profile'}))
]
