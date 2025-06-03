import json
from django.core.paginator import Paginator
from django.views import View

# from apps.menu.models import RoleMenu
from apps.role.models import Role
from service_error.common import COMMON_RERROR
from service_error.role import ROLE_RERROR
from apps.role.models import RoleSerializer
from common.response import ResponseSuccess, ResponseError


class CreateView(View):
    def post(self, request):
        role = json.loads(request.body)
        rol = Role.objects.create(name=role['name'], code=role['code'], remark=role['remark'])
        menus = role['menus']
        # roleId = rol.id
        # for menu in menus:
        #     SysRoleMenu.objects.create(menu_id=menu, role_id=roleId)
        # return ResponseSuccess()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        roleLists = Paginator(Role.objects.filter(is_deleted=0), pageSize).page(pageNo)
        total = Role.objects.filter(is_deleted=0).count()
        roles = RoleSerializer(roleLists.object_list.values(), many=True).data
        data = {'lists': roles, 'total': total, 'pageSize': pageSize, 'pageNo': pageNo}
        return ResponseSuccess(data=data)


class SearchListsView(View):
    def get(self, request):
        roleLists = Role.objects.filter(is_deleted=0)
        roles = RoleSerializer(roleLists.all(), many=True).data
        return ResponseSuccess(data=roles)


class UpdateView(View):
    def post(self, request):
        data = json.loads(request.body)
        id = data.get('id')
        role = Role.objects.filter(id=id).update(name=data['name'], code=data['code'],
                                                 remark=data['remark'])
        # RoleMenu.objects.filter(role_id=id).delete()
        # for menu in data['menus']:
        #     RoleMenu.objects.update_or_create(menu_id=menu, role_id=id)
        # return ResponseSuccess()


class DetailView(View):
    def post(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        role = Role.objects.get(id=role_id)
        # roleinfo = RoleSerializer(role).data
        # menus = list(RoleMenu.objects.filter(role_id=role_id).all().values_list('menu_id', flat=True))
        # data = {**roleinfo, 'menus': menus}
        # return ResponseSuccess(data=data)


class DeleteView(View):
    def delete(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        role = Role.objects.get(id=role_id)
        role.is_deleted = 1
        role.save()
        return ResponseSuccess()
