from rest_framework import serializers
from .models import *
from rest_framework import exceptions
from django.contrib.auth import authenticate, login


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email_address', 'phone_number', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# we must have to update the sceanirio for the updating the password also


# ******************************************************************
# varification serializer
# *******************************************************************
class EmailVarificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Varification
        fields = '__all__'


# ******************************************************************
# Email OTP  serializer
# *******************************************************************

class EmailOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOtp
        fields = '__all__'


# ******************************************************************
# User Profile serializer
# *******************************************************************

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
