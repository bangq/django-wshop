from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'password', 'email', 'token', 'head_img', 'mobile', 'is_customer')


class LogoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email')
