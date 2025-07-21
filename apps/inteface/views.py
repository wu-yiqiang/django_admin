import json
from sqlite3 import IntegrityError
from django.core.paginator import Paginator
from apps.inteface.models import Inteface, IntefaceSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage
from service_error.common import COMMON_RERROR
from service_error.menu import MENU_RERROR
from rest_framework.viewsets import ViewSet


class IntefaceViewSet(ViewSet):
    def list(self, request):
        try:
            intefaces = Inteface.objects.filter(is_deleted=0)
            intefaceLists = IntefaceSerializer(intefaces.values(), many=True).data
            return ResponseSuccess(data=intefaceLists)
        except IntegrityError:
            return ResponseError()

    def create(self, request):
        menu = json.loads(request.body)
        try:
            Inteface.objects.create(name=menu['name'], path=menu['path'], type=menu['type'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def destroy(self, request, inteface_id):
        if inteface_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            Inteface.objects.filter(id=inteface_id).delete()
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def update(self, request):
        menu = json.loads(request.body)
        id = menu.get('id')
        try:
            Inteface.objects.filter(id=id).update(name=menu['name'], path=menu['path'], type=menu['type'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def details(self, request, inteface_id):
        if inteface_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            inteface = Inteface.objects.get(id=inteface_id)
            intefaceInfo = IntefaceSerializer(inteface).data
            return ResponseSuccess(data=intefaceInfo)
        except IntegrityError:
            return ResponseError()

    def retrieve(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        try:
            roleLists = Paginator(Inteface.objects.filter(is_deleted=0), pageSize).page(pageNo)
            total = Inteface.objects.filter(is_deleted=0).count()
            intefaces = IntefaceSerializer(roleLists.object_list.values(), many=True).data
            return ResponseSuccessPage(data=intefaces, total=total, pageSize=pageSize, pageNo=pageNo)
        except IntegrityError:
            return ResponseError()
