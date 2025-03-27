from django.http import JsonResponse


def ResponseSuccess(code=200, data=None, msg='Operation Success'):
    return JsonResponse({'code': code, 'data': data, 'msg': msg})


def ResponseError(data):
    return JsonResponse(data)
