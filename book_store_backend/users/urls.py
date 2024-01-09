from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("register/", views.Register.as_view(), name="register"),
    path("change-password/", views.ChangePassword.as_view(), name="change_password"),
    path("list/", views.UserList.as_view(), name="UserList"),
    path("list/<int:pk>/", views.RetrieveUpdateDestroyUser.as_view(),
         name="RetrieveUpdateDestroyUser"),
]
