from django.db import models
from datetime import datetime

# Create your models here.

# **********************************************************
# Post  Model
# *********************************************************


class Post(models.Model):
    post_header = models.CharField(max_length=100, unique=True, null=False)
    post_Name = models.CharField(max_length=100, unique=True, null=True)
    post_content = models.CharField(max_length=1000, null=True)
    post_author = models.CharField(max_length=50, null=True)
    post_created_dt = models.DateTimeField(default=datetime.now, null=True)
    post_updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


# **********************************************************
# Post  Model
# *********************************************************


class Category(models.Model):
    post_header = models.ForeignKey(
        Post, to_field='post_header', on_delete=models.CASCADE)
    post_category_name = models.CharField(max_length=50, null=True)
    post_category_description = models.CharField(max_length=200, null=True)
    post_category_created_dt = models.DateTimeField(
        default=datetime.now, null=True)
    post_category_updated_dt = models.DateTimeField(
        default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Review(models.Model):
    post_header = models.ForeignKey(
        Post, to_field='post_header', on_delete=models.CASCADE)
    post_review = models.CharField(max_length=50, unique=True, null=False)
    post_reviewed_by = models.CharField(max_length=50, unique=True, null=False)
    post_reviewed_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
