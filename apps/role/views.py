import json
from django.core.paginator import Paginator
from django.views import View

from apps.menu.models import SysRoleMenu
from apps.role.models import SysRole
from service_error.common import COMMON_RERROR
from service_error.role import ROLE_RERROR
from apps.role.models import SysRoleSerializer
from common.response import ResponseSuccess, ResponseError


class CreateView(View):
    def post(self, request):
        role = json.loads(request.body)
        rol = SysRole.objects.create(name=role['name'], code=role['code'], remark=role['remark'])
        menus = role['menus']
        roleId = rol.id
        for menu in menus:
            print('roleId', menu)
            SysRoleMenu.objects.create(menu_id=menu, role_id=roleId)
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
        role = SysRole.objects.filter(id=id).update(name=data['name'], code=data['code'],
                                                    remark=data['remark'])
        SysRoleMenu.objects.filter(role_id=id).delete()
        for menu in data['menus']:
            SysRoleMenu.objects.update_or_create(menu_id=menu, role_id=id)
        return ResponseSuccess()


class DetailView(View):
    def post(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        role = SysRole.objects.get(id=role_id)
        roleinfo = SysRoleSerializer(role).data
        menus = list(SysRoleMenu.objects.filter(role_id=role_id).all().values_list('menu_id', flat=True))
        data = {**roleinfo, 'menus': menus}
        return ResponseSuccess(data=data)


class DeleteView(View):
    def delete(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        role = SysRole.objects.get(id=role_id)
        role.is_deleted = 1
        role.save()
        return ResponseSuccess()
