from django.http import JsonResponse


def Response(code=200, data=None, msg='Operation Success'):
    return JsonResponse({'code': code, 'data': data, 'msg': msg})
