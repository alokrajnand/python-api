from rest_framework import serializers
from .models import *
from rest_framework import exceptions
from django.contrib.auth import authenticate, login

# ******************************************************************
# Post serializer
# *******************************************************************


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
