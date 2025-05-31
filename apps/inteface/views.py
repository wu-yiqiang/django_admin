import json
from django.core.paginator import Paginator
from django.views import View
from apps.inteface.models import Inteface, IntefaceSerializer
from common.response import ResponseSuccess, ResponseError
from service_error.common import COMMON_RERROR
from service_error.menu import MENU_RERROR


class CreateView(View):
    def post(self, request):
        menu = json.loads(request.body)
        Inteface.objects.create(name=menu['name'], path=menu['path'], type=menu['type'])
        return ResponseSuccess()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        roleLists = Paginator(Inteface.objects.filter(is_deleted=0), pageSize).page(pageNo)
        total = Inteface.objects.filter(is_deleted=0).count()
        roles = IntefaceSerializer(roleLists.object_list.values(), many=True).data
        data = {'lists': roles, 'total': total, 'pageSize': pageSize, 'pageNo': pageNo}
        return ResponseSuccess(data=data)


class UpdateView(View):
    def post(self, request):
        menu = json.loads(request.body)
        id = menu.get('id')
        menu = Inteface.objects.filter(id=id).update(name=menu['name'], path=menu['path'], type=menu['type'])
        return ResponseSuccess()


class DetailView(View):
    def get(self, request, inteface_id):
        if inteface_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        inteface = Inteface.objects.get(id=inteface_id)
        intefaceInfo = IntefaceSerializer(inteface).data
        return ResponseSuccess(data=intefaceInfo)


class DeleteView(View):
    def delete(self, request, inteface_id):
        if inteface_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        Inteface.objects.filter(id=inteface_id).delete()
        return ResponseSuccess()
