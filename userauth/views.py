
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
# importing "random" for random operations
import random

# ****************************************************
# USER REGISTRATION PROCESS
# ****************************************************


@csrf_exempt
def UserViewSet(request, format=None):

    if request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # generate otp
            otp = GenerateOtp()
            print(otp)

            # save otp to the otp table
            email = serializer.data.get('email_address')
            print(email)
            EmailOtp.objects.create(
                email_address_id=email,
                email_otp=otp,
                counter=1
            )
            # send mail to the email address

            # redirect to the varification page -- done at fron end

            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


# **********************************************************
# post views for the login and send some user information
# *********************************************************


class LoginViewSet(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # TO get data from the request object
        user = request.data.get('username')

        # validate that user exists in the database
        data = User.objects.filter(email_address=user)
        if (data.count() == 0):
            return Response({
                'message': 'User does not exists',
                'status': 400
            })
        # to check user phone and email is  validated
        # Login process
        else:
            serializer = self.serializer_class(
                data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'email_address': user.email_address,
                'name': user.name
            })

# **********************************************************
# post view for the email varification
# *********************************************************


class VarificationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def post_auth(self, request, *args, **kwargs):
        # post method to validate the key

        email = request.data.get('email_address')
        print(email)
        otp = request.data.get('email_otp')
        print(otp)

        # get otp from the table
        data = EmailOtp.objects.get(email_address_id=email)
        print(data.email_address_id)
        print(data.email_otp)

        # compare the otp
        if (otp == data.email_otp):
            print("otp matches")
            # create a data in the varification table
            Varification.objects.create(
                email_address_id=email, email_varification="done")
            # remove the entry of otp from the otp table
            return Response({"every thing is good"})
        else:
            print("no match")
            return Response({"no otp match"})


# ******************************************************************
# sent mail function
# *******************************************************************


def SendEmail(email_address):
    subject = "Email Varification"
    message = "Please find the key here"
    from_email = "alok_kumar@nanduniversity.com"
    to_email = email_address

    send_mail(subject, message, from_email, [to_email], fail_silently=False,)

# ******************************************************************
# generate OTP function
# *******************************************************************


def GenerateOtp():
    return (random.randrange(100000, 999999))
