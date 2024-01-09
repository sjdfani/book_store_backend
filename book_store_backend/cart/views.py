from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cart, PurchaseItem
from .serializers import (
    CartSerializer,
)


class GetCart(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
