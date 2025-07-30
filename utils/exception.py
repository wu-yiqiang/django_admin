import json

from rest_framework.exceptions import APIException


class BusinessException(APIException):
    def __init__(self, data=None):
        self.status_code = 200
        self.detail = data
