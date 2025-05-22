import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from rest_framework_jwt.settings import api_settings
from apps.menu.models import SysRoleMenu, SysMenu
from apps.role.models import SysRole, SysUserRole, SysRoleSerializer
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from .models import Button, SysButtonSerializer
from common.response import ResponseSuccess, ResponseError


class CreateView(View):
    def post(self, request):
        button = json.loads(request.body)
        btn = Button.objects.create(name=button['name'], code=button['code'])
        return ResponseSuccess()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        buttonLists = Paginator(Button.objects.filter(is_deleted=0), pageSize).page(pageNo)
        total = Button.objects.filter(is_deleted=0).count()
        print('sdsd', buttonLists.object_list)
        buttons = SysButtonSerializer(buttonLists.object_list.values(), many=True).data
        data = {'lists': buttons, 'total': total, 'pageSize': pageSize, 'pageNo': pageNo}
        return ResponseSuccess(data=data)


class SearchListsView(View):
    def post(self, request):
        return ResponseSuccess()


class UpdateView(View):
    def post(self, request):
        data = json.loads(request.body)
        id = data.get('id')
        button = Button.objects.filter(id=id).update(name=data['name'], code=data['code'])
        return ResponseSuccess()


class DetailView(View):
    def post(self, request, button_id):
        if button_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        button = Button.objects.get(id=button_id)
        buttonDetails = SysButtonSerializer(button).data
        return ResponseSuccess(data=buttonDetails)


class DeleteView(View):
    def delete(self, request, button_id):
        if button_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        button = Button.objects.get(id=button_id)
        button.delete()
        button.save()
        return ResponseSuccess()
