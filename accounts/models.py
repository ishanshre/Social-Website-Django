from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
    

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d/', blank=True, default='default.png')
    bio = models.TextField()
