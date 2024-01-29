from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseItem
from .serializers import (
    CreatePurchaseItemSerializer, ChangeCountOfPurchaseItemSerializer,
    PaymentSerializer, PurchaseItemSerializer, RemovePurchaseItemSerializer,
    GetIDPurchaseItemSerializer,
)


class AddPurchaseItem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CreatePurchaseItemSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemovePurchaseItem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RemovePurchaseItemSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


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
        if status_ in ("true", "false"):
            status_ = True if status_ == "true" else False
            return PurchaseItem.objects.filter(
                user=self.request.user,
                status=status_,
            )
        return PurchaseItem.objects.none()


class GetIDPurchaseItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetIDPurchaseItemSerializer

    def get_queryset(self):
        return PurchaseItem.objects.filter(user=self.request.user, status=True)
