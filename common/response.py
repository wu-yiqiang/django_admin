from django.http import JsonResponse
from service_error.common import COMMON_RERROR


def ResponseSuccess(code=200, data=None, msg='Operation Success'):
    return JsonResponse({'code': code, 'data': data, 'msg': msg})


def ResponseError(data=COMMON_RERROR.SERVICE_ERROR):
    return JsonResponse(data)
