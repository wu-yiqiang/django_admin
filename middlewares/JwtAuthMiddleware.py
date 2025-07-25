from heapq import merge

import jwt
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.settings import api_settings
from common.response import ResponseError, ResponseSuccess
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from django.core.cache import cache
from utils.redisTool import get_cache


class JwtAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/user/login', '/user/logout', '/user/register', '/swagger', '/schema']
        path = request.path
        if path not in white_list and not path.startswith('/storage'):
            try:
                token = request.META.get('HTTP_AUTHORIZATION')
                exist = cache.has_key(token)
                if exist is False:
                    return JsonResponse(COMMON_RERROR.TOKEN_EXPIRED, status=401)
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                user_dict = jwt_decode_handler(token)
                user_id = user_dict['user_id']
                if (user_id is None or user_id == ""):
                    return JsonResponse(USER_RERROR.USER_IS_EMPTY)
                if (self.auth_api(token, path) is False):
                    return ResponseError(COMMON_RERROR.IS_NOT_AUTH)
            except jwt.ExpiredSignatureError as e:
                return JsonResponse(COMMON_RERROR.TOKEN_EXPIRED, status=401)
            except jwt.InvalidTokenError as e:
                return JsonResponse(COMMON_RERROR.TOKEN_VERIFICATION_FAILED, status=401)
            except Exception as e:
                print("500", e)
                return JsonResponse(COMMON_RERROR.TOKEN_VERIFICATION_EXCEPTION, status=500)
        else:
            return None

    def auth_api(self, token, path):
        userInfo = get_cache(token)
        intefaces = userInfo.get('intefaces')
        intefaceLists = [inteface.get('path') for inteface in intefaces]
        return True
        for inteface_path in intefaceLists:
            if inteface_path in path:
                return True
        return False
