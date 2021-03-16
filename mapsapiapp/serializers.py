from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:

        model=Users
        fields=['username',
                'password',
                'email',
                'first_name',
                'last_name']