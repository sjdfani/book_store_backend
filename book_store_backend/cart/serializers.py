from rest_framework import serializers
from books.models import Book
from books.serializers import BookSerializer
from .models import PurchaseItem
from .utils import str_generator


class PurchaseItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = PurchaseItem
        fields = "__all__"


class GetIDPurchaseItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseItem
        fields = ("book",)


class CreatePurchaseItemSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )
    count = serializers.IntegerField()

    def create(self, validated_data, user):
        return PurchaseItem.objects.create(
            user=user,
            book=validated_data["book"],
            count=validated_data["count"],
        )

    def save(self, **kwargs):
        user = self.context["request"].user
        self.create(self.validated_data, user)


class RemovePurchaseItemSerializer(serializers.Serializer):
    purchase_item = serializers.PrimaryKeyRelatedField(
        queryset=PurchaseItem.objects.all()
    )

    def save(self, **kwargs):
        obj = self.validated_data["purchase_item"]
        obj.delete()


class ChangeCountOfPurchaseItemSerializer(serializers.Serializer):
    purchase_item = serializers.PrimaryKeyRelatedField(
        queryset=PurchaseItem.objects.all()
    )
    count = serializers.IntegerField()

    def save(self, **kwargs):
        obj = self.validated_data["purchase_item"]
        obj.count = self.validated_data["count"]
        obj.save()


class PaymentSerializer(serializers.Serializer):

    def payment_process(self, **kwargs):
        user = self.context["request"].user
        transaction_id = str_generator(8, True)
        items = PurchaseItem.objects.filter(user=user, status=True)
        for item in items:
            item.bought_done(transaction_id)
