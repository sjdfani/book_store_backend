from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, PurchaseItem
from .serializers import (
    CartSerializer, CreatePurchaseItemSerializer, ChangeCountOfPurchaseItemSerializer,
    PaymentSerializer, PurchaseItemSerializer,
)


class GetCart(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class AddPurchaseItem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CreatePurchaseItemSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeCountOfPurchaseItem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ChangeCountOfPurchaseItemSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class Payment(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = PaymentSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.payment_process()
        return Response(status=status.HTTP_200_OK)


class PurchaseItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseItemSerializer

    def get_queryset(self):
        status_ = self.kwargs.get("status")
        if status_ in ("True", "False"):
            status_ = True if status_ == "True" else False
            return PurchaseItem.objects.filter(
                user=self.request.user,
                status=status_,
            )
        return PurchaseItem.objects.none()
