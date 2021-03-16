from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone
# Create your models here.


class Users(models.Model):
    username=models.CharField(max_length=15,unique=True)
    password=models.CharField(max_length=25)
    email=models.EmailField(max_length=25,unique=True)
    joined=models.DateTimeField(default=timezone.now())
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=15)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['password','email']


    def __str__(self):
        return self.username
     






