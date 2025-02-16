import json
from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.settings import api_settings
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from user.models import SysUser


class LoginView(View):
    def post(self, request):
        try:
            params = json.loads(request.body)
        except Exception as e:
            return HttpResponse(COMMON_RERROR.DATA_PARSE_ERROR['msg'])
        username = params.get("username")
        password = params.get('password')
        if username is None or password is None:
            return HttpResponse(USER_RERROR.USER_AND_PASSWORD_IS_REQUIRED['msg'])
        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return HttpResponse(token)

        except Exception as e:
            print(e)
            return HttpResponse(USER_RERROR.USER_OR_PASSWORD_ERROR['msg'])
        return HttpResponse("post")


class UserView(View):
    def get(self, request):
        return HttpResponse("获取用户列表")

    def post(self, request):
        return HttpResponse("新增用户")
