from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field(blank=True, null=True, config_name='extends')
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(blank=True, max_length=100)
    category = models.CharField(max_length=100, default='uncategorised')
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')

    def number_of_likes(self):
        return self.likes.count()
