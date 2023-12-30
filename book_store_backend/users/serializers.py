from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ("password",)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if not get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is not exists.")
        return value
