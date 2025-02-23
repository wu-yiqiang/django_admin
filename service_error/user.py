# @Desc: { 项目响应码模块 }
class USER_RERROR:
    USER_IS_NOT_EXIST = {"code": 20000001, 'msg': "user is not exist", 'data': None}
    USER_OR_PASSWORD_ERROR = {"code": 20000002, "msg": "user or password error", 'data': None}
    USER_AND_PASSWORD_IS_REQUIRED = {'code': 20000003, 'msg': "user and password is required", 'data': None}
    USER_IS_EMPTY = {'code': 20000004, 'msg': "User Is Empty", 'data': None}
