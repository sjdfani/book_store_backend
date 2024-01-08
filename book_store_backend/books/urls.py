from django.urls import path
from .views import (
    BookList, RetrieveBook, CreateBook, AllBookList, RetrieveUpdateDestroyAllBook,
    CreateSaveItem, DestroySaveItem, SaveItemList,
)

app_name = "books"

urlpatterns = [
    path("list/", BookList.as_view(), name="BookList"),
    path("list/<int:pk>/", RetrieveBook.as_view(), name="RetrieveBook"),
    path("create/", CreateBook.as_view(), name="CreateBook"),
    path("all/list/", AllBookList.as_view(), name="AllBookList"),
    path("all/list/<int:pk>/", RetrieveUpdateDestroyAllBook.as_view(),
         name="RetrieveUpdateDestroyAllBook"),
    path("saveItem/create/", CreateSaveItem.as_view(), name="CreateSaveItem"),
    path("saveItem/remove/", DestroySaveItem.as_view(), name="DestroySaveItem"),
    path("saveItem/list/", SaveItemList.as_view(), name="SaveItemList"),
]
