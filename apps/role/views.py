import json
from datetime import datetime
from sqlite3 import IntegrityError
from django.core.paginator import Paginator
from django.db import transaction
from django.views import View
from rest_framework.viewsets import ViewSet
from apps.role.models import Role
from common.request import requestSerializer
from common.validate import request_verify
from common.errors import COMMON_RERROR
from common.errors import ROLE_RERROR
from apps.role.models import RoleSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage
import logging

logger = logging.getLogger('django')


class RoleViewSet(ViewSet):
    def list(self, request):
        try:
            roleLists = Role.objects.filter(is_deleted=0)
            roles = RoleSerializer(roleLists.all(), many=True).data
            return ResponseSuccess(data=roles)
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()

    def create(self, request):
        roleData = json.loads(request.body)
        try:
            with transaction.atomic():
                role = Role.objects.create(name=roleData['name'], code=roleData['code'], remark=roleData['remark'],
                                           create_time=datetime.now())
                role.menus.set(roleData.get('menus'))
                role.intefaces.set(roleData.get('intefaces'))
                role.buttons.set(roleData.get('buttons'))
            return ResponseSuccess()
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()

    def destroy(self, request, role_id):
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

    def update(self, request):
        data = json.loads(request.body)
        id = data.get('id')
        try:
            with transaction.atomic():
                role = Role.objects.filter(id=id).update(name=data['name'], code=data['code'],
                                                         remark=data['remark'])
                roleobj = Role.objects.get(id=id)
                roleobj.menus.set(data.get('menus'))
                roleobj.intefaces.set(data.get('intefaces'))
                roleobj.buttons.set(data.get('buttons'))
                return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    @request_verify('post', ['pageSize', 'pageNo'])
    def retrieve(self, request):
        params = requestSerializer(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        try:
            roleLists = Paginator(Role.objects.filter(is_deleted=0, name__icontains=params.get('search')),
                                  pageSize).page(pageNo)
            total = Role.objects.filter(is_deleted=0).count()
            roles = RoleSerializer(roleLists.object_list.values(), many=True).data
            return ResponseSuccessPage(data=roles, total=total, pageSize=pageSize, pageNo=pageNo)
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()

    def details(self, request, role_id):
        if role_id is None:
            return ResponseError(ROLE_RERROR.ROLE_ID_IS_NOT_EXIST)
        try:
            role = Role.objects.get(id=role_id)
            roleinfo = RoleSerializer(role).data
            return ResponseSuccess(data=roleinfo)
        except IntegrityError as e:
            logger.error(e)
            return ResponseError()
