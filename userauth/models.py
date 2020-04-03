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


# **********************************************************
# Create User Processing
# *********************************************************
class MyUserManager(BaseUserManager):

    def create_user(self, username, phone_number, name, email_address, date_of_birth, password=None):
        if not username:
            raise ValueError('Valid user name is Required')

        if not phone_number:
            raise ValueError('Valid Phone Number is Required')

        if not email_address:
            raise ValueError('Valid Email Addreess is Required')

        if not name:
            raise ValueError('You Must have name')

        user_obj = self.model(
            username=username,
            phone_number=phone_number,
            name=name,
            email_address=self.normalize_email(email_address),
            date_of_birth=date_of_birth,

        )

        user_obj.set_password(password)
        user_obj.is_admin = False
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, phone_number, name,  email_address, date_of_birth, password=None):

        user_obj = self.create_user(
            username=username,
            phone_number=phone_number,
            email_address=self.normalize_email(email_address),
            name=name,
            date_of_birth=date_of_birth,
            password=password,
        )
        user_obj.is_admin = True
        user_obj.save(using=self._db)
        return user_obj


# code for user model

class User(AbstractBaseUser):

    username = models.CharField(max_length=50, unique=True, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="phone number is not valid")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, unique=True)
    email_address = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50, unique=False, blank=False)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number',
                       'date_of_birth', 'email_address', 'name']

    def __str__(self):
        return self.username

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

class CredentialVarification(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=False)
    phone_number = models.CharField(max_length=50, unique=True, null=False)
    Email_varification_code = models.CharField(max_length=200, null=True)
    phone_otp_code = models.IntegerField()
    email_otp_code = models.IntegerField()
    varification_status = models.BooleanField()
    code_sent_counter = models.IntegerField()

    def __str__(self):
        return self.Email_varification_code


# **********************************************************
# Profile Model
# *********************************************************

class UserProfile(models.Model):
    username = models.OneToOneField(
        User, null=False, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, unique=True, null=False)
    email_address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=2)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.username
