from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="profile/", blank =True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)


