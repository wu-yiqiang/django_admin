import copy
from functools import wraps
import json
from django.http import HttpResponse

from service_error.common import COMMON_RERROR
from utils.exception import BusinessException


def request_verify(request_method: str, param_lists=None):
    def decorator(func):
        @wraps(func)
        def inner(self, request, *args, **kwargs):
            method = str(request.method).lower()
            if method != request_method.lower():
                raise BusinessException(COMMON_RERROR.REQUEST_METHOD_ERROR)
            request.params = {}
            if method == 'post':
                try:
                    data = json.loads(request.body.decode('utf-8'))
                except Exception as e:
                    raise BusinessException(COMMON_RERROR.SERVICE_ERROR)
                if not data or data == {}:
                    if param_lists is not None:
                        raise BusinessException(COMMON_RERROR.PARAMS_IS_NULL)
                for param in param_lists:
                    if data.get(param) is None:
                        PARAM_IS_NULL = COMMON_RERROR.PARAM_IS_NULL.copy()
                        PARAM_IS_NULL['msg'] = param + PARAM_IS_NULL.get('msg')
                        raise BusinessException(PARAM_IS_NULL)
            return func(self, request, *args, **kwargs)

        return inner

    return decorator
