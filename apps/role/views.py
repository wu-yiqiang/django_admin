import json
from sqlite3 import IntegrityError

from django.core.paginator import Paginator
from django.db import transaction
from django.views import View

# from apps.menu.models import RoleMenu
from apps.role.models import Role
from service_error.common import COMMON_RERROR
from service_error.role import ROLE_RERROR
from apps.role.models import RoleSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage
import logging

logger = logging.getLogger('django')


class CreateView(View):
    def post(self, request):
        roleData = json.loads(request.body)
        try:
            with transaction.atomic():
                role = Role.objects.create(name=roleData['name'], code=roleData['code'], remark=roleData['remark'])
                role.menus.set(roleData.get('menus'))
                role.intefaces.set(roleData.get('intefaces'))
                role.buttons.set(roleData.get('buttons'))
            return ResponseSuccess()
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        try:
            roleLists = Paginator(Role.objects.filter(is_deleted=0), pageSize).page(pageNo)
            total = Role.objects.filter(is_deleted=0).count()
            roles = RoleSerializer(roleLists.object_list.values(), many=True).data
            return ResponseSuccessPage(data=roles, total=total, pageSize=pageSize, pageNo=pageNo)
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()


class SearchListsView(View):
    def get(self, request):
        try:
            roleLists = Role.objects.filter(is_deleted=0)
            roles = RoleSerializer(roleLists.all(), many=True).data
            return ResponseSuccess(data=roles)
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()


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
        try:
            role = Role.objects.get(id=role_id)
            roleinfo = RoleSerializer(role).data
            print(role, roleinfo)
            return ResponseSuccess()
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()
        # roleinfo = RoleSerializer(role).data
        # menus = list(RoleMenu.objects.filter(role_id=role_id).all().values_list('menu_id', flat=True))
        # data = {**roleinfo, 'menus': menus}
        # return ResponseSuccess(data=data)


class DeleteView(View):
    def delete(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        try:
            role = Role.objects.get(id=role_id)
            role.is_deleted = 1
            role.save()
            return ResponseSuccess()
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()
