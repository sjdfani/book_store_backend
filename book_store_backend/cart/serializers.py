from rest_framework import serializers
from rest_framework.validators import ValidationError
from books.models import Book
from books.serializers import BookSerializer
from .models import Cart, PurchaseItem
from .utils import str_generator


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class PurchaseItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True)

    class Meta:
        model = PurchaseItem
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


class PaymentSerializer(serializers.Serializer):

    def validate(self, attrs):
        cart = Cart.objects.filter(user=self.context["request"].user)
        if cart.exists():
            if len(cart.purchase_items.all()) == 0:
                raise ValidationError({"message": "Your cart is empty"})
            raise ValidationError({"message": "You don't have open cart"})
        return attrs

    def payment_process(self, **kwargs):
        user = self.context["request"].user
        transaction_id = str_generator(15, True)
        cart = Cart.objects.get(user=user)
        cart.complete_payment(transaction_id)
