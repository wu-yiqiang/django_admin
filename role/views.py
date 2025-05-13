import json
import math
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from rest_framework_jwt.settings import api_settings
from role.models import SysRole
from service_error.common import COMMON_RERROR
from service_error.role import ROLE_RERROR
from role.models import User, SysRoleSerializer
from common.response import ResponseSuccess, ResponseError


class CreateView(View):
    def post(self, request):
        role = json.loads(request.body)
        SysRole.objects.create(name=role['name'], code=role['code'], remark=role['remark'])
        return ResponseSuccess()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        roleLists = Paginator(SysRole.objects.filter(is_deleted=0), pageSize).page(pageNo)
        total = SysRole.objects.filter(is_deleted=0).count()
        roles = SysRoleSerializer(roleLists.object_list.values(), many=True).data
        data = {'lists': roles, 'total': total, 'pageSize': pageSize, 'pageNo': pageNo}
        return ResponseSuccess(data=data)


class SearchListsView(View):
    def get(self, request):
        roleLists = SysRole.objects.filter(is_deleted=0)
        roles = SysRoleSerializer(roleLists.all(), many=True).data
        return ResponseSuccess(data=roles)


class UpdateView(View):
    def post(self, request):
        data = json.loads(request.body)
        id = data.get('id')
        user = SysRole.objects.filter(id=id).update(name=data['name'], code=data['code'],
                                                    remark=data['remark'])
        return ResponseSuccess()


class DetailView(View):
    def post(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        role = SysRole.objects.get(id=role_id)
        roleinfo = SysRoleSerializer(role).data
        return ResponseSuccess(data=roleinfo)


class DeleteView(View):
    def delete(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        role = SysRole.objects.get(id=role_id)
        role.is_deleted = 1
        role.save()
        return ResponseSuccess()
