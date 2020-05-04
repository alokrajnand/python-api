from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', SchoolViewSet.as_view({'get': 'get'})),
    path('<name>', SchoolViewSet.as_view({'get': 'get_detail'})),
    path('gallery/<name>',
         SchoolGalleryViewSet.as_view({'get': 'get_detail'})),
    path('fee/<name>', SchoolFeeViewSet.as_view({'get': 'get_detail'})),
    path('facilities/<name>',
         SchoolFacilityViewSet.as_view({'get': 'get_detail'})),
]

