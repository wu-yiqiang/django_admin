from django.http import JsonResponse
from common.errors import COMMON_RERROR


def ResponseSuccess(code=200, data=None, msg='Operation Success'):
    return JsonResponse({'code': code, 'data': data, 'msg': msg})


def ResponseError(data=COMMON_RERROR.SERVICE_ERROR):
    return JsonResponse(data)


def ResponseSuccessPage(code=200, data=None, total=0, pageSize=0, pageNo=0, msg='Operation Success'):
    return JsonResponse(
        {'code': code, 'data': data, 'total': total, 'pageSize': pageSize, 'pageNo': pageNo, 'msg': msg})
