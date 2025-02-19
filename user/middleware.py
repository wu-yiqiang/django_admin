import jwt
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.settings import api_settings


class JwtAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/user/login']
        path = request.path
        if path not in white_list and not path.startswith('/midia'):
            try:
                token = request.META.get('HTTP_AUTHORIZATION')
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                jwt_decode_handler(token)
            except jwt.ExpiredSignatureError as e:
                return HttpResponse({'data': {}, 'msg': "token expired"})
            except jwt.InvalidTokenError as e:
                return HttpResponse({'code': 500, 'msg': 'token验证失败', 'data': {}})
            except Exception as e:
                return HttpResponse({'code': 500, 'msg': 'token验证异常', 'data': {}})
        pass
