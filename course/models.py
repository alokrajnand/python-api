from django.db import models
from datetime import datetime
# Create your models here.

# **********************************************************
# Course  Model
# *********************************************************


class Course(models.Model):
    course_header = models.CharField(max_length=50, unique=True, null=False)
    course_name = models.CharField(max_length=50, unique=True, null=False)
    course_category = models.CharField(max_length=50, unique=True, null=False)
    course_author = models.CharField(max_length=50, null=True)
    course_short_desc = models.CharField(max_length=100, null=True)
    course_desc = models.CharField(max_length=5000, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Faq(models.Model):
    faq_id = models.IntegerField()
    course_header = models.ForeignKey(
        Course, to_field='course_header', on_delete=models.CASCADE)
    question = models.CharField(max_length=50, unique=True, null=False)
    answer = models.CharField(max_length=50, unique=True, null=False)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Review(models.Model):
    course_header = models.ForeignKey(
        Course, to_field='course_header', on_delete=models.CASCADE)
    review_comment = models.CharField(max_length=500, null=False)
    reviewed_by = models.CharField(max_length=50, unique=True)
    course_video_quality = models.CharField(max_length=50, unique=True)
    course_content_quality = models.CharField(max_length=50, unique=True)
    course_engagging_quality = models.CharField(max_length=50, unique=True)
    course_sound_quality = models.CharField(max_length=50, unique=True,)
    star_rating = models.IntegerField()
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


# **********************************************************
# Lesson  Model
# *********************************************************

class Category(models.Model):
    course_header = models.ForeignKey(
        Course, to_field='course_header', on_delete=models.CASCADE)
    course_category_id = models.CharField(
        max_length=50, unique=True, null=False)
    course_category_name = models.CharField(
        max_length=50, unique=True, null=False)
    course_category_desc = models.CharField(
        max_length=5000, unique=False, null=False)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


# **********************************************************
# Lesson  Model
# *********************************************************

class Lesson(models.Model):
    course_header = models.ForeignKey(
        Course, to_field='course_header', on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50, unique=True, null=False)
    lesson_description = models.CharField(
        max_length=100, unique=True, null=False)
    lesson_video_link = models.CharField(
        max_length=50, unique=True, null=False)
    lesson_about = models.CharField(max_length=1000, null=False)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
