import json
from sqlite3 import IntegrityError
from rest_framework.viewsets import ViewSet
from django.core.paginator import Paginator
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from apps.button.models import Button, ButtonSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage


class ButtonViewSet(ViewSet):
    def list(self, request):
        try:
            buttons = Button.objects.filter(is_deleted=0)
            buttonsLists = ButtonSerializer(buttons.values(), many=True).data
            return ResponseSuccess(data=buttonsLists)
        except IntegrityError:
            return ResponseError()

    def retrieve(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        try:
            buttonLists = Paginator(Button.objects.filter(is_deleted=0), pageSize).page(pageNo)
            total = Button.objects.filter(is_deleted=0).count()
            buttons = ButtonSerializer(buttonLists.object_list.values(), many=True).data
            return ResponseSuccessPage(data=buttons, total=total, pageSize=pageSize, pageNo=pageNo)
        except IntegrityError:
            return ResponseError()

    def create(self, request):
        button = json.loads(request.body)
        try:
            Button.objects.create(name=button['name'], code=button['code'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def update(self, request):
        data = json.loads(request.body)
        id = data.get('id')
        try:
            Button.objects.filter(id=id).update(name=data['name'], code=data['code'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def destroy(self, request, button_id):
        if button_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            button = Button.objects.get(id=button_id)
            button.delete()
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def details(self, request, button_id):
        if button_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            button = Button.objects.get(id=button_id)
            buttonDetails = ButtonSerializer(button).data
            return ResponseSuccess(data=buttonDetails)
        except IntegrityError:
            return ResponseError()
