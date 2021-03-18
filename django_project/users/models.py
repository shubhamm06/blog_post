from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/')

    instagram_url = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'
