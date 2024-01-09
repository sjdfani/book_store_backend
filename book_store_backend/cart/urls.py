from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("list/", views.GetCart.as_view(), name="GetCart"),
    path("purchase_item/create/", views.AddPurchaseItem.as_view(),
         name="AddPurchaseItem"),
    path("change-count/", views.ChangeCountOfPurchaseItem.as_view(),
         name="ChangeCountOfPurchaseItem"),
    path("payment/", views.Payment.as_view(), name="Payment"),
    path("purchase_item/list/<bool:status>/",
         views.PurchaseItemList.as_view(), name="PurchaseItemList"),
]
