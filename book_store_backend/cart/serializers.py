from rest_framework import serializers
from books.models import Book
from .models import Cart, PurchaseItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CreatePurchaseItemSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )
    count = serializers.IntegerField()

    def create(self, validated_data, user):
        obj = PurchaseItem.objects.create(
            book=validated_data["book"],
            count=validated_data["count"],
        )
        cart = Cart.objects.get_or_create(user=user)[0]
        cart.add_purchase_item(obj)

    def save(self, **kwargs):
        user = self.context["request"].user
        self.create(self.validated_data, user)


class ChangeCountOfPurchaseItemSerializer(serializers.Serializer):
    purchase_item = serializers.PrimaryKeyRelatedField(
        queryset=PurchaseItem.objects.all()
    )
    count = serializers.IntegerField()

    def save(self, **kwargs):
        obj = self.validated_data["purchase_item"]
        obj.count = self.validated_data["count"]
        obj.save()
