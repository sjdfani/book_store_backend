from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperuser
from .models import Book, SaveItem
from .serializers import (
    BookSerializer, SaveItemSerializer, CreateSaveItemSerializer,
    DestroySaveItemSerializer,
)


class BookList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
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
    queryset = Book.objects.all()


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
    serializer_class = DestroySaveItemSerializer

    def get_queryset(self):
        return SaveItem.objects.filter(user=self.request.user)


class SaveItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveItemSerializer

    def get_queryset(self):
        return SaveItem.objects.filter(user=self.request.user)
