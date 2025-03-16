from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=True)
