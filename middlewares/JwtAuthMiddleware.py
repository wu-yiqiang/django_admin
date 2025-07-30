import jwt
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.settings import api_settings
from django_admin import settings
from common.const import REQUEST_LIMIT_PREFIX, REQUESTS_LIMITS
from common.response import ResponseError
from common.errors import COMMON_RERROR, USER_RERROR
from django.core.cache import cache
from utils.redis import get_cache, set_cache


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

            limits_str = get_cache(REQUEST_LIMIT_PREFIX + token)
            limits = int(limits_str or 0)
            if limits >= REQUESTS_LIMITS:
                return ResponseError(COMMON_RERROR.SERVICE_BUSY)
            else:
                set_cache(REQUEST_LIMIT_PREFIX + token, limits + 1, settings.REQUEST_LIMIT_EXPIRE)
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
