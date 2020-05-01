
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

# ****************************************************
# USER REGISTRATION PROCESS
# ****************************************************


@csrf_exempt
def UserViewSet(request, format=None):

    if request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)

        # check if phone number is provided
        # check name is given
        # check if a valid email id is provided
        # check if date of birth is given

        # if all the above condition are valid check phone number exists in the myuser table or not
        # if phone number exists you are all ready registered  please login or go to forget password
        # if phone number does not exists  then send the otp and varification link to the email address and redirct the user to the varification page

        # Check if varification is success full
        # check if phone varification is ok
        # check if email varification is ok
        # if both the varification is ok then register the user and redirect to the login page

        # this will happen only when the phone otp and mail id varification will be done
        ''' send_mail(
            'Subject here',
            'Here is the message.',
            'alok_kumar@nanduniversity.com',
            ['alokrajnand@gmail.com'],
            fail_silently=False,
        ) '''
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


# **********************************************************
# post views for the login and send some user information
# *********************************************************


class LoginViewSet(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'name': user.name
        })

# **********************************************************
# Logout mechnaism
# *********************************************************


# ******************************************************************
# To Get profil Information if user is authenticated and logged in
# *******************************************************************


class ProfileViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = self.request.user
        print(user)
        data = UserProfile.objects.filter(username=user)
        user = UserProfileSerializer(data, many=True)
        return Response(user.data)


