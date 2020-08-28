
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
from django.db import Error

# ****************************************************
# USER REGISTRATION PROCESS
# ****************************************************


@csrf_exempt
def UserViewSet(request, format=None):

    if request.method == "POST":
        print(request.body)
        json_parser = JSONParser()
        data = json_parser.parse(request)

        print('ok')
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            # generate otp
            serializer.save()
            email = serializer.data.get('email_address')
            otp = GenerateOtp(email)
            # send mail to the email address
            print(otp)

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
        print(request.data)
        user = request.data.get('username')

        # validate that user exists in the database
        email = User.objects.filter(email_address=user)
        # if user does not exists in the database send massage need to register
        if (email.count() == 0):
            return Response({
                'message': 'User does not exists Please Sign Up',
                'status': 400
            })
        # If user exists in the data base check for the varification
        else:
            email_active = Varification.objects.filter(email_address_id=user)
            # if data for the user daoes not exists in the varification table
            if (email_active.count() == 0):
                # generate otp and send and ask for varification redirect it to varification page
                otp = GenerateOtp(user)
                print(otp)
                return Response({
                    'message': 'User data does not exists in the varification table',
                    'status': 400
                })

            # if data for the user exists in the varification table then cheack the varification status
            else:
                # validate the validation and counter accordingly respons
                data = Varification.objects.get(email_address_id=user)
                # check the varification status on the varification table if not varified
                if (data.email_varification != 'done'):
                    # generate otp and send and ask for varification redirect it to varification page
                    otp = GenerateOtp(user)
                    print(otp)
                    return Response({
                        'message': 'User data exists in the varification table but not varified',
                        'status': 400
                    })
                # If varification is allready in the varification table
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
        otp = request.data.get('email_otp')
        otp = int(otp)
        # get otp from the table
        try:
            data = EmailOtp.objects.get(email_address_id=email)
            # compare the otp
            if (otp == data.email_otp):
                # cretae a entry in the varification table
                Varification.objects.filter(email_address_id=email).create(
                    email_address_id=email,
                    email_varification='done'
                )
                # varification successfulle please login
                return Response('varification successfulle please login')
            else:
                return Response('varification unsuccessfulle please check OTP')

        except EmailOtp.DoesNotExist:
            return Response("no data in the otp table")


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


def GenerateOtp(email_address):
    # return (random.randrange(100000, 999999))
    # check otp exists in the otp table or not
    try:
        data = EmailOtp.objects.get(email_address_id=email_address)
        print(data.counter)
        otp = (random.randrange(100000, 999999))
        EmailOtp.objects.filter(email_address_id=email_address).update(
            email_otp=otp,
            counter=data.counter+1
        )
        return otp
    except EmailOtp.DoesNotExist:
        # otp generated
        otp = (random.randrange(100000, 999999))
        # save otp to the otp table
        EmailOtp.objects.create(
            email_address_id=email_address,
            email_otp=otp,
            counter=1
        )
        return otp


# ******************************************************************
# user  profile viewset
# *******************************************************************

class ProfileViewSet(viewsets.ViewSet):

    permission_classes = [AllowAny]

    def get_profile(self, request, name, *args, **kwargs):
        user_profile = Profile.objects.get(email_address=name)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    # insert data to profile when signup

    def post_profile(self, request, *args, **kwargs):
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    # Update profile data
    def put_profile(self, request, name, pk=None):
        user_profile = Profile.objects.get(email_address=name)
        serializer = UserProfileSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
