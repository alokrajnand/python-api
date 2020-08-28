from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
# write the code of user manager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime

# **********************************************************
# Create User Processing
# *********************************************************


class MyUserManager(BaseUserManager):

    def create_user(self, email_address, phone_number, name, password=None):

        user_obj = self.model(
            email_address=self.normalize_email(email_address),
            phone_number=phone_number,
            name=name
        )

        user_obj.set_password(password)
        user_obj.is_admin = False
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email_address, phone_number, name, password=None):

        user_obj = self.create_user(
            email_address=self.normalize_email(email_address),
            phone_number=phone_number,
            name=name,
            password=password,
        )
        user_obj.is_admin = True
        user_obj.save(using=self._db)
        return user_obj


# code for user model

class User(AbstractBaseUser):

    email_address = models.EmailField(max_length=255, unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="phone number is not valid")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, unique=True)
    name = models.CharField(max_length=50, unique=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['phone_number', 'name']

    def __str__(self):
        return self.email_address

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# To create a token as soon as user register

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# **********************************************************
# mail and phone validation model and processing
# *********************************************************

class Varification(models.Model):
    email_address = models.OneToOneField(
        User, to_field='email_address', on_delete=models.CASCADE)
    email_varification = models.CharField(max_length=20, null=True)
    phone_varification = models.CharField(max_length=20, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class EmailOtp(models.Model):
    email_address = models.OneToOneField(
        User, to_field='email_address', on_delete=models.CASCADE)
    email_otp = models.IntegerField()
    counter = models.IntegerField()

    def __str__(self):
        return self.__all__

# **********************************************************
# Profile Model
# *********************************************************


class Profile(models.Model):
    email_address = models.OneToOneField(
        User, to_field='email_address', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="phone number is not valid")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, unique=True)
    user_designation = models.CharField(max_length=200, null=True)
    user_tag_line = models.CharField(max_length=200, null=True)
    user_tag_line_desc = models.CharField(max_length=300, null=True)
    user_date_of_birth = models.DateField(null=True)
    user_profile_pic_link = models.CharField(max_length=200, null=True)
    user_banner_pic_link = models.CharField(max_length=200, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_city = models.CharField(max_length=60, null=True)
    user_state = models.CharField(max_length=60, null=True)
    user_country = models.CharField(max_length=60, null=True)
    user_twitter_link = models.CharField(max_length=200, null=True)
    user_git_hub_link = models.CharField(max_length=200, null=True)
    user_linkdin_link = models.CharField(max_length=200, null=True)
    user_faebook_link = models.CharField(max_length=200, null=True)
    user_instagram_link = models.CharField(max_length=200, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
