from heapq import merge

import jwt
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.settings import api_settings
from service_error.common import COMMON_RERROR


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
                return JsonResponse(COMMON_RERROR.TOKEN_EXPIRED)
            except jwt.InvalidTokenError as e:
                return JsonResponse(COMMON_RERROR.TOKEN_VERIFICATION_FAILED)
            except Exception as e:
                return JsonResponse(COMMON_RERROR.TOKEN_VERIFICATION_EXCEPTION)
        else:
            return None
