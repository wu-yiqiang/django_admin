import json
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from pycparser.ply.yacc import token
from rest_framework_jwt.settings import api_settings
from role.models import SysRole
from service_success.common import COMMON_SUCCESS
from service_error.user import USER_RERROR
from service_success.common import COMMON_SUCCESS
from user.models import SysUser, SysUserSerializer
from rest_framework import authtoken


class RegisterView(View):
    def post(self, request):
        pass


class LoginView(View):
    def post(self, request):
        params = json.loads(request.body)
        if params['username'] is None:
            return JsonResponse(USER_RERROR.USERNAME_IS_EMPTY)
        if params['password'] is None:
            return JsonResponse(USER_RERROR.PASSWORD_IS_EMPTY)
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
            role_list = SysRole.objects.raw(
                "SELECT id, name,FROM sys_role WHERE id IN (SELECT role_id FROM sys_uer_role WHERE user_id = " + str(
                    user.id) + ")")
        except Exception as e:
            print(e)
            return HttpResponse(USER_RERROR.USER_OR_PASSWORD_ERROR['msg'])
        return JsonResponse(
            {"code": 200, "data": {"token": token, "data": SysUserSerializer(user).data, "msg": 'success'}})


class CreateView(View):
    # def get(self, request):
    #     return HttpResponse("获取用户列表")
    def post(self, request):
        print("萨达")
        return HttpResponse("新增用户")


class UpdatePasswordView(View):
    def post(self, request):
        params = json.loads(request.body)
        if params['username'] is None:
            return JsonResponse(USER_RERROR.USERNAME_IS_EMPTY)
        if params['password'] is None:
            return JsonResponse(USER_RERROR.PASSWORD_IS_EMPTY)
        try:
            user = SysUser.objects.get(username=params['username'])
            user.password = params['password']
            user.save()
        except Exception as e:
            return JsonResponse(USER_RERROR.USER_PASSWORD_UPDATE_FAILED)
        return JsonResponse(COMMON_SUCCESS.OPEARTIN_SUCCESS)


class UpdateView(View):
    # def get(self, request):
    #     return HttpResponse("获取用户列表")
    def put(self, request):
        print("更新用户数据", request)
        return HttpResponse("更新用户数据")


class LogoutView(View):
    def post(self, request):
        print("更新用户数据", request.session.get('user_id'))
        tokens = authtoken.models.Token.objects.filter(expires__lt=datetime.now())
        tokens.delete()
        return JsonResponse(COMMON_SUCCESS.EXIT_SUCCESS)
