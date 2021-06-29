from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    email = models.EmailField()
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    resume = models.ImageField(upload_to='resume')
    profile_pic = models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return self.user.email