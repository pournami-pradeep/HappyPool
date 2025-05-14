from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    profile_photo = models.FileField(upload_to="media/profiles",null=True,blank=True)
    license_number = models.CharField(max_length=16)
    role = models.CharField(max_length=10)

class Test(models.Model):
    label = models.CharField(max_length=10)