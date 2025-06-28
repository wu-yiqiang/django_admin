from heapq import merge

import jwt
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.settings import api_settings

from apps.role.models import RoleSerializer
from apps.user.models import UserSerializer, User
from service_error.common import COMMON_RERROR
from service_error.user import USER_RERROR
from django.core.cache import cache


class JwtAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/user/login', '/user/register', '/swagger', '/schema']
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
                # if (self.auth_api(user_id, path) is False):
                #     return JsonResponse(COMMON_RERROR.IS_NOT_AUTH)
            except jwt.ExpiredSignatureError as e:
                return JsonResponse(COMMON_RERROR.TOKEN_EXPIRED, status=401)
            except jwt.InvalidTokenError as e:
                return JsonResponse(COMMON_RERROR.TOKEN_VERIFICATION_FAILED, status=401)
            except Exception as e:
                print("500", e)
                return JsonResponse(COMMON_RERROR.TOKEN_VERIFICATION_EXCEPTION, status=500)
        else:
            return None

    def auth_api(self, user_id, path):
        user = User.objects.get(id=user_id)
        intefaces = []
        permissions = user.roles.prefetch_related('menus').all()
        userPermissions = RoleSerializer(permissions, many=True).data
        for userPermission in userPermissions:
            inteface = userPermission.get('intefaces')
            if (inteface and inteface not in intefaces):
                intefaces = intefaces + [item['path'] for item in inteface]
        if (path not in intefaces):
            return False
        return True
