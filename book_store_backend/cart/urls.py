from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("list/", views.GetCart.as_view(), name="GetCart"),
    path("purchase_item/create/", views.AddPurchaseItem.as_view(),
         name="AddPurchaseItem"),
]
