from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("purchase_item/create/", views.AddPurchaseItem.as_view(),
         name="AddPurchaseItem"),
    path("purchase_item/remove/", views.RemovePurchaseItem.as_view(),
         name="RemovePurchaseItem"),
    path("purchase_item/count/", views.ChangeCountOfPurchaseItem.as_view(),
         name="ChangeCountOfPurchaseItem"),
    path("payment/calculate/", views.Payment.as_view(), name="Payment"),
    path("payment/confirm/", views.ConfirmPayment.as_view(), name="ConfirmPayment"),
    path("purchase_item/list/<str:status>/",
         views.PurchaseItemList.as_view(), name="PurchaseItemList"),
    path("purchase_item/id/",
         views.GetIDPurchaseItemList.as_view(), name="GetIDPurchaseItemList"),
]
