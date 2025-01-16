from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class User(models.Model ):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    tokens = models.IntegerField(default=4000)
    token = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.message
    

    

