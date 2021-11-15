import requests
from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from . import serializers


class UserActivationView(views.APIView):

    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response({"message": "Аккаунт подтвержден" if content == "" else content},
                        status=status.HTTP_201_CREATED)


class PasswordResetView(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordSerializer

    def get(self, request, uid, token):
        return Response({"message": "Введите новый пароль дважды."},
                        status=status.HTTP_204_NO_CONTENT)

    def post(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/auth/users/reset_password_confirm/"
        post_data = {'uid': uid, 'token': token,
                     'new_password': request.POST['new_password'], 're_new_password': request.POST['re_new_password']}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response({"message": "Пароль сменен" if content == "" else content},
                        status=status.HTTP_205_RESET_CONTENT)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = serializers.LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Пользователь вышел"},
                        status=status.HTTP_204_NO_CONTENT)
