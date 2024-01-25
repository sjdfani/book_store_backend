from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password",)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is not exists.")
        return value


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    fullname = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if CustomUser.objects.filter(email=attrs["email"]).exists():
            raise ValidationError({"message": "This email is exists."})
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError(
                {"message": "Your input passwords are not match"})
        return attrs

    def create(self, validated_data, password):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def save(self, **kwargs):
        self.validated_data.pop("password")
        password = self.validated_data.pop("confirm_password")
        return self.create(self.validated_data, password)


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = self.context["request"].user
        if not user.check_password(attrs["current_password"]):
            raise ValidationError({"message": "Your password is incorrect."})
        if attrs["new_password"] != attrs["confirm_password"]:
            raise ValidationError(
                {"message": "The input passwords are not match."})
        return attrs

    def change_password(self):
        user = self.context["request"].user
        new_password = self.validated_data["new_password"]
        user.set_password(new_password)
        user.save()
