# @Desc: { 项目响应码模块 }
from enum import Enum, unique


class COMMON_RERROR:
    SERVICE_ERROR = {"code": 10000000, "msg": "System Error", "data": None}
    DATA_PARSE_ERROR = {"code": 10000001, "msg": "Data Parse Error", "data": None}
    TOKEN_EXPIRED = {"code": 10000002, "msg": "Token Expired", "data": None}
    TOKEN_VERIFICATION_FAILED = {"code": 10000003, "msg": "Token Verification Failed", "data": None}
    TOKEN_VERIFICATION_EXCEPTION = {"code": 10000004, "msg": "Token Verification Exception", "data": None}
    PAGENATE_PARAMS_IS_EMPTY = {"code": 10000005, "msg": "Pagenate Params Is Empty", "data": None},
    FILE_UPLOAD_IS_FAILED = {"code": 10000006, "msg": "File Upload Failed", "data": None}
    ID_IS_EMPTY = {"code": 10000007, "msg": "Query ID Is Empty", "data": None}
    IS_NOT_AUTH = {"code": 10000008, "msg": "The interface is not authorized.", "data": None}
    REQUEST_METHOD_ERROR = {"code": 10000009, "msg": "The request method is error.", "data": None}
