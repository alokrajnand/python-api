from rest_framework import serializers
from .models import *
from rest_framework import exceptions


# ******************************************************************
# course serializer
# *******************************************************************

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseFaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = "__all__"


class CourseRevieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
