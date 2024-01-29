from rest_framework import serializers
from .models import Book, SaveItem
from users.models import CustomUser
from rest_framework.validators import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class SaveItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = SaveItem
        fields = "__all__"


class GetIDSaveItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaveItem
        fields = ("book",)


class CreateSaveItemSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    def validate(self, attrs):
        if SaveItem.objects.filter(user=attrs["user"], book=attrs["book"]).exists():
            raise ValidationError({"message": "You saved this book before"})
        return attrs

    def create(self, validated_data):
        return SaveItem.objects.create(
            user=validated_data["user"],
            book=validated_data["book"],
        )


class DestroySaveItemSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all()
    )
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    def validate(self, attrs):
        if not SaveItem.objects.filter(user=attrs["user"], book=attrs["book"]).exists():
            raise ValidationError(
                {"message": "You didn't save this book before"})
        return attrs

    def save(self, **kwargs):
        obj = SaveItem.objects.get(
            user=self.validated_data["user"], book=self.validated_data["book"])
        obj.delete()
