import json
import math
from datetime import datetime
from tokenize import Number

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.template.backends.django import reraise
from django.views import View
from pycparser.ply.yacc import token
from rest_framework_jwt.settings import api_settings
from role.models import SysRole
from service_error.user import USER_RERROR
from user.models import User, SysUserSerializer
from rest_framework import authtoken
from common.response import Response


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
            user = User.objects.get(username=username, password=password)
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
        data = {**SysUserSerializer(user).data, 'token': token}
        return Response(data=data)


class CreateView(View):
    # def get(self, request):
    #     return HttpResponse("获取用户列表")
    def post(self, request):
        print("萨达")
        user = json.loads(request.body)
        print(user)
        User.objects.create(username=user['username'], password=user['password'], avatar=user['avatar'],
                            email=user['email'], phone_number=user['phoneNumber'], status=user['status'])
        return Response()


class pageView(View):
    def post(self, request):
        return Response()


class UpdatePasswordView(View):
    def post(self, request):
        params = json.loads(request.body)
        if params['username'] is None:
            return JsonResponse(USER_RERROR.USERNAME_IS_EMPTY)
        if params['password'] is None:
            return JsonResponse(USER_RERROR.PASSWORD_IS_EMPTY)
        try:
            user = User.objects.get(username=params['username'])
            user.password = params['password']
            user.save()
        except Exception as e:
            return JsonResponse(USER_RERROR.USER_PASSWORD_UPDATE_FAILED)
        # return JsonResponse(COMMON_SUCCESS.OPEARTIN_SUCCESS)


class UpdateView(View):
    # def get(self, request):
    #     return HttpResponse("获取用户列表")
    def put(self, request):
        print("更新用户数据", request)
        return HttpResponse("更新用户数据")


class LogoutView(View):
    def post(self, request):
        print("更新用户数据", request.session.get('user_id'))
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        # token, _ = authtoken.models.Token.objects.get_or_create(user=user_id)
        # token = authtoken.models.Token.objects.filter(user=user).first()
        # authtoken.
        # token.delete()
        # return JsonResponse(COMMON_SUCCESS.EXIT_SUCCESS)


class GetAssetsView(View):
    def get(self, request):
        page_size = request.GET.get("pageSize")
        page_no = request.GET.get("pageNo")
        datas = []
        for i in range(1, int(page_size)):
            item_dict = {
                'id': math.radians(),
                'title': "椅子",
                'categopry': "办公用品",
                'department': "人事行政部",
                'number': "FZC00",
                'status': 0,
                'assetsStatus': 1,
                'belong': "sutter",
                'updator': "Tom",
                'update': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
            datas.append(item_dict)
        print(datas)
        return JsonResponse({'code': 200, 'data': json.dumps(datas), 'msg': 'success'})
