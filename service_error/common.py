# @Desc: { 项目响应码模块 }
from enum import Enum, unique


class COMMON_RERROR(Enum):
    DATA_PARSE_ERROR = {"code": 10000001, 'msg': "data parse error"}
