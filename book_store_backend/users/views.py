from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
import serializers
from .utils import get_tokens_for_user


class Login(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = get_user_model().objects.get(username=username)
        if user.check_password(password):
            user.update_last_login()
            message = {
                "user": serializers.UserSerializer(user).data,
                "tokens": get_tokens_for_user(user)
            }
            return Response(message, status=status.HTTP_200_OK)
        message = {"message": "email or password is incorrect."}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class Register(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
