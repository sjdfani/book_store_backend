from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from .models import CustomUser
from . import serializers
from .utils import get_tokens_for_user
from .permissions import IsSuperuser


class Login(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = CustomUser.objects.get(email=email)
        if user.check_password(password):
            user.update_last_login()
            message = {
                "user": serializers.UserSerializer(user).data,
                "tokens": get_tokens_for_user(user)
            }
            return Response(message, status=status.HTTP_200_OK)
        message = {"message": "Email or password is incorrect."}
        return Response(message, status=status.HTTP_401_UNAUTHORIZED)


class Register(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RegisterSerializer
    queryset = CustomUser.objects.all()


class ChangePassword(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = serializers.ChangePasswordSerializer(
            data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.change_password()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserList(generics.ListAPIView):
    permission_classes = (IsSuperuser,)
    serializer_class = serializers.UserSerializer
    queryset = CustomUser.objects.all()


class RetrieveUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user.email)


class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperuser,)
    serializer_class = serializers.UserSerializer
    queryset = CustomUser.objects.all()
