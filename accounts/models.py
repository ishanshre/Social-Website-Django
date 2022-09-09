from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.urls import reverse
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True,null=True)
    

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d/', blank=True, default='profile_photo/default.png')
    bio = models.TextField()
    country = CountryField(blank=True, null=True, default=None)
    following = models.ManyToManyField(get_user_model(), related_name='following', blank=True)
    def total_followers(self):
        return self.following.count()

    def list_followers(self):
        return self.following.all()

    def profiles_post(self):
        return self.posts.all()   

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 

    def get_success_url(self):
        post_id = self.get_object()
        return reverse('accounts:profile_detail', kwargs={'pk':post_id.pk})
        
