from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsSuperuser
from .models import Book, SaveItem
from .serializers import (
    BookSerializer, SaveItemSerializer, CreateSaveItemSerializer,
    DestroySaveItemSerializer,
)


class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(publish=True)


class RetrieveBook(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.filter(publish=True)


class CreateBook(generics.CreateAPIView):
    permission_classes = (IsSuperuser,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AllBookList(generics.ListAPIView):
    permission_classes = (IsSuperuser,)
    serializer_class = BookSerializer
    queryset = Book.objects.order_by("pk")


class RetrieveUpdateDestroyAllBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperuser,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateSaveItem(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateSaveItemSerializer
    queryset = SaveItem.objects.all()


class DestroySaveItem(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = DestroySaveItemSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SaveItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveItemSerializer

    def get_queryset(self):
        return SaveItem.objects.filter(user=self.request.user)


class PopularList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        state = self.kwargs.get("state", None)
        if state == 0:
            return Book.objects.filter(publish=True).order_by("-rating")[:5]
        elif state == 1:
            return Book.objects.filter(publish=True).order_by("-rating")
        else:
            return Book.objects.none()


class NewestList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(publish=True).order_by("-pk")[:2]

    def get_queryset(self):
        state = self.kwargs.get("state", None)
        if state == 0:
            return Book.objects.filter(publish=True).order_by("-pk")[:2]
        elif state == 1:
            return Book.objects.filter(publish=True).order_by("-pk")
        else:
            return Book.objects.none()
