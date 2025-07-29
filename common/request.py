from service_error.common import COMMON_RERROR
import json


def requestSerializer(data):
    params = json.loads(data)
    return params
