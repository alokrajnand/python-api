from rest_framework import serializers
from .models import *
from rest_framework import exceptions
from django.contrib.auth import authenticate, login

# ******************************************************************
# School serializer
# *******************************************************************


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"


# ******************************************************************
# School Fee serializer
# *******************************************************************

class SchoolFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = "__all__"

# ******************************************************************
# School Gallery serializer
# *******************************************************************


class SchoolGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = "__all__"


class SchoolFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = "__all__"
