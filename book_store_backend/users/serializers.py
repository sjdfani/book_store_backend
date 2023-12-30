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


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    fullname = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if get_user_model().objects.filter(username=attrs["username"]).exists():
            raise ValidationError({"message": "This username is exists."})
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError(
                {"message": "Your input passwords are not match"})
        return attrs

    def create(self, validated_data, password):
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def save(self, **kwargs):
        self.validated_data.pop("password")
        password = self.validated_data.pop("confirm_password")
        return self.create(self.validated_data, password)
