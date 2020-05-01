from django.db import models

# Create your models here.

# **********************************************************
# Post  Model
# *********************************************************


class Post(models.Model):
    post_id = models.IntegerField()
    post_header = models.CharField(max_length=50, unique=True, null=False)
    post_content = models.CharField(max_length=50, unique=True, null=False)
    post_author = models.CharField(max_length=200, null=True)
    post_created_date = models.DateField(null=True)
    post_updated_date = models.DateField(null=True)

    def __str__(self):
        return self.__all__
