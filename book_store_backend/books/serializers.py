from rest_framework import serializers
from .models import Book, SaveItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class SaveItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = SaveItem
        fields = "__all__"
