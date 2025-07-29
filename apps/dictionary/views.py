import json
from sqlite3 import IntegrityError
from apps.dictionary.models import Dictionary, DictionarySerializer
from django.core.paginator import Paginator
from django.views import View

from common.request import requestSerializer
from common.validate import request_verify
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from rest_framework.viewsets import ViewSet
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage


class DictionaryViewSet(ViewSet):
    def list(self, request):
        pass

    def create(self, request):
        dictionary = json.loads(request.body)
        try:
            Dictionary.objects.create(type=dictionary['type'], code=dictionary['code'], label=dictionary['label'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def update(self, request):
        dictionary = json.loads(request.body)
        id = dictionary.get('id')
        try:
            Dictionary.objects.filter(id=id).update(type=dictionary['type'], code=dictionary['code'],
                                                    label=dictionary['label'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def destroy(self, request, dictionary_id):
        if dictionary_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            dictionary = Dictionary.objects.get(id=dictionary_id)
            dictionary.delete()
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    @request_verify('post', ['pageSize', 'pageNo'])
    def retrieve(self, request):
        params = requestSerializer(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        try:
            dictLists = Paginator(Dictionary.objects.filter(is_deleted=0, type__icontains=params.get('search')),
                                  pageSize).page(pageNo)
            total = Dictionary.objects.filter(is_deleted=0).count()
            dicts = DictionarySerializer(dictLists.object_list.values(), many=True).data
            return ResponseSuccessPage(data=dicts, total=total, pageSize=pageSize, pageNo=pageNo)
        except Exception as e:
            print(e)
            return ResponseError()

    def details(self, request, dictionary_id):
        if dictionary_id is None:
            return ResponseError(USER_RERROR.USER_ID_IS_NOT_EXIST)
        try:
            dictionary = Dictionary.objects.get(id=dictionary_id)
            dictionaryDetails = DictionarySerializer(dictionary).data
            return ResponseSuccess(data=dictionaryDetails)
        except IntegrityError:
            return ResponseError()

    def types(self, request):
        data = json.loads(request.body)
        type = data['type']
        try:
            dictionarys = Dictionary.objects.filter(is_deleted=0).filter(type=type)
            dictionaryLists = DictionarySerializer(dictionarys.values(), many=True).data
            return ResponseSuccess(data=dictionaryLists)
        except IntegrityError:
            return ResponseError()
