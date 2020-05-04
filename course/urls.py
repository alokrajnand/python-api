from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'get'})),
    path('<name>', CourseViewSet.as_view({'get': 'get_detail'})),
    path('review/<name>', CourseViewSet.as_view({'get': 'get_review_detail'})),
    path('faq/<name>', CourseViewSet.as_view({'get': 'get_faq_detail'})),
    path('lesson/<name>', LessonViewSet.as_view({'get': 'get_detail'})),

]
