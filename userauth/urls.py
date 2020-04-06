from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('register/', UserViewSet),
    path('login/', LoginViewSet.as_view()),
    path('profile/', ProfileViewSet.as_view()),
    path('posts/', PostViewSet.as_view({'get': 'get'})),
    path('posts/<id>/', PostViewSet.as_view({'get': 'get_detail'})),
]
