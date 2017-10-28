from django.db import models

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField('date')
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    image = models.CharField(max_length=500)
    body = models.TextField()


    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)


    def __str__(self):
        return self.name
