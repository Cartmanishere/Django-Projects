from django.db import models
import datetime
from django.contrib.auth.models import User

class Link(models.Model):
    title = models.CharField(max_length=200, default="")
    date = models.DateTimeField('date')
    TAG_CHOICES = (
    ("Movie", "Movie"),
    ("Game", "Game"),
    ("TV", "TV"),
    ("Tutorial", "Tutorial"),
    ("Music", "Music"),
    ("Ebook", "Ebook"),
    )
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default="")
    link = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    size = models.CharField(max_length=10, default="")
    user = models.ForeignKey(User, related_name='user', default=1)

    def __str__(self):
        return self.title
        return self.tag

