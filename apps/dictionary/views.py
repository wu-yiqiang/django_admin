import json
from sqlite3 import IntegrityError

from django.core.paginator import Paginator
from django.views import View
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from .models import Dictionary, DictionarySerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage


class CreateView(View):
    def post(self, request):
        dictionary = json.loads(request.body)
        try:
            Dictionary.objects.create(type=dictionary['type'], code=dictionary['code'], label=dictionary['label'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        try:
            dictLists = Paginator(Dictionary.objects.filter(is_deleted=0), pageSize).page(pageNo)
            total = Dictionary.objects.filter(is_deleted=0).count()
            dicts = DictionarySerializer(dictLists.object_list.values(), many=True).data
            return ResponseSuccessPage(data=dicts, total=total, pageSize=pageSize, pageNo=pageNo)
        except IntegrityError:
            return ResponseError()


class SearchTypeListsView(View):
    def post(self, request):
        data = json.loads(request.body)
        type = data['type']
        try:
            dictionarys = Dictionary.objects.filter(is_deleted=0).filter(type=type)
            dictionaryLists = DictionarySerializer(dictionarys.values(), many=True).data
            return ResponseSuccess(data=dictionaryLists)
        except IntegrityError:
            return ResponseError()


class UpdateView(View):
    def post(self, request):
        dictionary = json.loads(request.body)
        id = dictionary.get('id')
        try:
            Dictionary.objects.filter(id=id).update(type=dictionary['type'], code=dictionary['code'],
                                                    label=dictionary['label'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()


class DetailView(View):
    def get(self, request, dictionary_id):
        if dictionary_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            dictionary = Dictionary.objects.get(id=dictionary_id)
            dictionaryDetails = DictionarySerializer(dictionary).data
            return ResponseSuccess(data=dictionaryDetails)
        except IntegrityError:
            return ResponseError()


class DeleteView(View):
    def delete(self, request, dictionary_id):
        if dictionary_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            dictionary = Dictionary.objects.get(id=dictionary_id)
            dictionary.delete()
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()
