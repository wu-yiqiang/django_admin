# @Desc: { 项目响应码模块 }
class ROLE_RERROR:
    ROLE_IS_NOT_EXIST = {"code": 30000001, 'msg': "role is not exist", 'data': None}
    ROLE_NAME_IS_EMPTY = {'code': 30000002, 'msg': "RoleName Is Empty", 'data': None}
    ROLE_INFO_UPDATE_FAILED = {'code': 30000003, 'msg': "Role Info Update Failed", 'data': None}
    ROLE_ID_IS_NOT_EXIST = {'code': 30000004, 'msg': "Role Id Not Exist", 'data': None}
