from django.db import models

# Create your models here.

# **********************************************************
# Course  Model
# *********************************************************


class Course(models.Model):
    course_id = models.IntegerField()
    course_header = models.CharField(max_length=50, unique=True, null=False)
    course_name = models.CharField(max_length=50, unique=True, null=False)
    course_category = models.CharField(max_length=50, unique=True, null=False)
    course_author = models.CharField(max_length=50, null=True)
    course_description = models.CharField(max_length=5000, null=True)
    course_created_date = models.DateField(null=True)
    course_cupdated_date = models.DateField(null=True)

    def __str__(self):
        return self.__all__


class Faq(models.Model):
    faq_id = models.IntegerField()
    course_id = models.IntegerField()
    course_header = models.CharField(max_length=50,  null=False)
    question = models.CharField(max_length=50, unique=True, null=False)
    answer = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.__all__


class Review(models.Model):
    comment_id = models.IntegerField()
    course_id = models.IntegerField()
    course_header = models.CharField(max_length=50, unique=True, null=False)
    comment_description = models.CharField(
        max_length=50, unique=True, null=False)
    comment_by = models.CharField(max_length=50, unique=True)
    course_review = models.CharField(max_length=50, unique=True)
    course_video_quality = models.CharField(max_length=50, unique=True)
    course_content_quality = models.CharField(max_length=50, unique=True)
    course_engagging_quality = models.CharField(max_length=50, unique=True)
    course_sound_quality = models.CharField(max_length=50, unique=True,)
    star_rating = models.IntegerField()
    comment_date = models.DateField(null=True)

    def __str__(self):
        return self.__all__


# **********************************************************
# Lesson  Model
# *********************************************************

class Category(models.Model):
    course_id = models.IntegerField()
    course_header = models.CharField(max_length=50, unique=True, null=False)
    course_category_id = models.CharField(
        max_length=50, unique=True, null=False)
    course_category_name = models.CharField(
        max_length=50, unique=True, null=False)
    course_category_description = models.CharField(
        max_length=5000, unique=False, null=False)

    def __str__(self):
        return self.__all__



# **********************************************************
# Lesson  Model
# *********************************************************

class Lesson(models.Model):
    course_id = models.IntegerField()
    course_header = models.CharField(max_length=50, unique=True, null=False)
    lesson_id = models.CharField(max_length=50, unique=True, null=False)
    lesson_name = models.CharField(max_length=50, unique=True, null=False)
    lesson_description = models.CharField(
        max_length=5000, unique=False, null=False)
    lesson_video_link = models.CharField(
        max_length=50, unique=True, null=False)

    def __str__(self):
        return self.__all__
