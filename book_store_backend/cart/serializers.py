from rest_framework import serializers

from .models import Cart, PurchaseItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
