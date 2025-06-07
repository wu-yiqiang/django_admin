import json
import math
from datetime import datetime
from django.core import serializers
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views import View
from openpyxl.styles.builtins import total
from rest_framework_jwt.settings import api_settings
from django.db import transaction
# from apps.menu.models import RoleMenu, Menu
# from apps.role.models import Role, UserRole, RoleSerializer
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from .models import User, UserSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage
from ..button.models import ButtonSerializer
from ..role.models import RoleSerializer, Role


class RegisterView(View):
    def post(self, request):
        pass


class LoginView(View):
    def post(self, request):
        params = json.loads(request.body)
        if params['email'] is None:
            return JsonResponse(USER_RERROR.USERNAME_IS_EMPTY)
        if params['password'] is None:
            return JsonResponse(USER_RERROR.PASSWORD_IS_EMPTY)
        email = params.get("email")
        password = params.get('password')
        user = User.objects.get(email=email, password=password)
        try:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
        except Exception as e:
            return ResponseError(USER_RERROR.USER_OR_PASSWORD_ERROR)
        try:
            userInfos = UserSerializer(user).data
            roles = user.roles.values()
            menus = []
            buttons = []
            intefaces = []
            permissions = user.roles.prefetch_related('menus').all()
            userPermissions = RoleSerializer(permissions, many=True).data
            for userPermission in userPermissions:
                menu = userPermission.get('menus')
                button = userPermission.get('buttons')
                inteface = userPermission.get('intefaces')
                if (menu and menu not in menus):
                    menus = menus + menu
                if (buttons and button not in buttons):
                    buttons = buttons + button
                if (inteface and inteface not in intefaces):
                    intefaces = intefaces + inteface
            data = {**userInfos, 'token': token, 'roles': list(roles), 'menus': menus,
                    'buttons': buttons,
                    'intefaces': intefaces}
            return ResponseSuccess(data=data)
        except Exception as e:
            return ResponseError()


class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            with transaction.atomic():
                user = User.objects.create(username=data['username'], password='1234@Abcd', avatar=data['avatar'],
                                           email=data['email'], phone_number=data['phone_number'],
                                           status=data['status'])
                user.roles.set(data.get('roles'))
            return ResponseSuccess()
        except Exception as e:
            print(e)
            return ResponseError()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        try:
            users = User.objects.filter(is_deleted=0)
            total = users.count()
            userLists = UserSerializer(Paginator(users, pageSize).page(pageNo), many=True).data
            return ResponseSuccessPage(data=userLists, total=total, pageSize=pageSize, pageNo=pageNo)
        except Exception as e:
            print(e)
            return ResponseError()


class SearchListsView(View):
    def post(self, request):
        return ResponseSuccess()


class UpdatePasswordView(View):
    def post(self, request):
        params = json.loads(request.body)
        if params['id'] is None:
            return JsonResponse(USER_RERROR.USER_IS_EMPTY)
        if params['password'] is None:
            return JsonResponse(USER_RERROR.PASSWORD_IS_EMPTY)
        try:
            user = User.objects.get(id=params['id'])
            user.password = params['password']
            user.save()
        except Exception as e:
            return ResponseError(USER_RERROR.USER_PASSWORD_UPDATE_FAILED)
        return ResponseSuccess()


class UpdateView(View):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data.get('id')
        try:
            user = User.objects.get(id=user_id)
            with transaction.atomic():
                User.objects.filter(id=user_id).update(username=data['username'], avatar=data['avatar'],
                                                       phone_number=data['phone_number'],
                                                       email=data['email'], status=data['status'])
                user.roles.set(data.get('roles'))
            return ResponseSuccess()
        except Exception as e:
            print(e)
            return ResponseError()


class DetailView(View):
    def post(self, request, user_id):
        if user_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            user = User.objects.get(id=user_id)
            roles = user.roles.values_list('id', flat=True)
            userInfo = UserSerializer(user).data
            data = {**userInfo, "roles": list(roles)}
            return ResponseSuccess(data=data)
        except Exception as e:
            return ResponseError()


class DeleteView(View):
    def delete(self, request, user_id):
        if user_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            user = User.objects.filter(id=user_id)
            user.delete()
            return ResponseSuccess()
        except Exception as e:
            return ResponseError()


class LogoutView(View):
    def post(self, request):
        return ResponseSuccess()


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


from openpyxl import Workbook


class ExportView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment;filename=user.xlsx'
        # 创建Workbook和Sheet
        workbook = Workbook()
        worksheet = workbook.active
        # 写入表头
        worksheet.cell(row=1, column=1, value='username')
        worksheet.cell(row=1, column=2, value='email')
        worksheet.cell(row=1, column=3, value='phone_number')
        worksheet.cell(row=1, column=4, value='remark')
        # 写入数据
        users = User.objects.all()
        for i, user in enumerate(users, start=2):
            worksheet.cell(row=i, column=1, value=user.username)
            worksheet.cell(row=i, column=2, value=user.email)
            worksheet.cell(row=i, column=3, value=user.phone_number)
            worksheet.cell(row=i, column=4, value=user.remark)
        workbook.save(response)
        return response


def ExportExcel():
    pass
