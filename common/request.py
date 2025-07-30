from common.errors import COMMON_RERROR
import json


def requestSerializer(data):
    params = json.loads(data)
    return params
