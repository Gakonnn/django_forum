from django.contrib.auth.models import User
from django.db import models


class Topics(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return self.name

class Rooms(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topics,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)

    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    body = models.TextField(max_length=2000,null=True)
    created = models.DateTimeField(auto_now= True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body[0:50]
