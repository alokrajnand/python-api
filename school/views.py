
# this is for login and logout authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
from django.shortcuts import render
# this is to send response to client
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # to resolve csrf issue
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
# model and serializer import
from .serializer import *
from .models import *
from django.core.mail import send_mail

# Create your views here.


# ******************************************************************
# Post
# *******************************************************************

class SchoolViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            data = School.objects.all()
            serializer = SchoolSerializer(data, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({
                'message': 'No Data',
                'status': 400
            })

    def get_detail(self, request, name):
        try:
            data = School.objects.get(school_header=name)
            serializer = SchoolSerializer(data)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({
                'message': 'No Data',
                'status': 400
            })


class SchoolFeeViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_detail(self, request, name):
        try:
            data = Fee.objects.get(school_header=name)
            serializer = SchoolFeeSerializer(data)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({
                'message': 'No Data',
                'status': 400
            })


class SchoolGalleryViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_detail(self, request, name):
        try:
            data = Gallery.objects.get(school_header=name)
            serializer = SchoolGallerySerializer(data)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({
                'message': 'No Data',
                'status': 400
            })


class SchoolFacilityViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_detail(self, request, name):
        try:
            data = Facility.objects.get(school_header=name)
            serializer = SchoolFacilitySerializer(data)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({
                'message': 'No Data',
                'status': 400
            })
