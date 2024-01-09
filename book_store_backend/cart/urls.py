from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("list/", views.GetCart.as_view(), name="GetCart"),
]
