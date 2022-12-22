from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]