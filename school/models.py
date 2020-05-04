from django.db import models
from datetime import datetime


# **********************************************************
# School  Model
# *********************************************************


class School(models.Model):
    school_header = models.CharField(max_length=100, unique=True, null=False)
    school_Name = models.CharField(max_length=100, unique=True, null=True)
    school_country = models.CharField(max_length=30, null=True)
    school_state = models.CharField(max_length=30, null=True)
    school_city = models.CharField(max_length=30, null=True)
    school_location = models.CharField(max_length=30, null=True)
    school_pincode = models.IntegerField()
    School_address = models.CharField(max_length=100, null=True)
    School_longitude = models.CharField(max_length=100, null=True)
    School_latitude = models.CharField(max_length=100, null=True)
    School_map_share_link = models.CharField(max_length=200, null=True)
    School_type = models.CharField(max_length=30, null=True)
    School_board = models.CharField(max_length=30, null=True)
    School_medium = models.CharField(max_length=30, null=True)
    School_owned_by = models.CharField(max_length=30, null=True)
    School_phone_number = models.CharField(max_length=30, null=True)
    School_website_url = models.CharField(max_length=50, null=True)
    School_mailing_address = models.CharField(max_length=50, null=True)
    School_about = models.CharField(max_length=2000, null=True)
    School_admission_process = models.CharField(max_length=1000, null=True)
    school_start_date = models.DateField(null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


# **********************************************************
# School  Model
# *********************************************************


class Fee(models.Model):
    school_header = models.ForeignKey(
        School, to_field='school_header', on_delete=models.CASCADE)
    grade = models.CharField(max_length=20, null=True)
    grade_desc = models.CharField(max_length=50, null=True)
    grade_fee = models.IntegerField()
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Gallery(models.Model):
    school_header = models.ForeignKey(
        School, to_field='school_header', on_delete=models.CASCADE)
    school_main_image_url = models.CharField(max_length=100, null=True)
    school_thumbnail_image_url = models.CharField(max_length=100, null=True)
    school_image_alt = models.CharField(max_length=100, null=True)
    school_image_desc = models.CharField(max_length=100, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Facility(models.Model):
    school_header = models.ForeignKey(
        School, to_field='school_header', on_delete=models.CASCADE)
    school_Library = models.CharField(max_length=10, null=True)
    school_playground = models.CharField(max_length=10, null=True)
    school_science_Lab = models.CharField(max_length=10, null=True)
    school_Computer_Lab = models.CharField(max_length=10, null=True)
    school_auditorium = models.CharField(max_length=10, null=True)
    school_music_club = models.CharField(max_length=10, null=True)
    school_drama_club = models.CharField(max_length=10, null=True)
    school_Swimming_pool = models.CharField(max_length=10, null=True)
    school_transport_facilities = models.CharField(max_length=10, null=True)
    school_smart_classroom = models.CharField(max_length=10, null=True)
    school_Number_of_teachers = models.CharField(max_length=10, null=True)
    school_number_of_class_room = models.CharField(max_length=10, null=True)
    school_student_per_classroom = models.CharField(max_length=10, null=True)
    school_disabled_friendly = models.CharField(max_length=10, null=True)
    school_hostel = models.CharField(max_length=10, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
