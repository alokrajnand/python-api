from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('', PostViewSet.as_view({'get': 'get'})),
    path('<name>', PostViewSet.as_view({'get': 'get_detail'})),
]
