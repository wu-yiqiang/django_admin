# @Desc: { 项目响应码模块 }
class USER_RERROR:
    USER_IS_NOT_EXIST = {"code": 20000001, "msg": "user is not exist", "data": None}
    EMAIL_OR_PASSWORD_ERROR = {"code": 20000002, "msg": "email or password error", "data": None}
    USER_AND_PASSWORD_IS_REQUIRED = {"code": 20000003, "msg": "user and password is Required", "data": None}
    USERNAME_IS_EMPTY = {"code": 20000004, "msg": "Username Is Required", "data": None}
    PASSWORD_IS_EMPTY = {"code": 20000005, "msg": "Password Is Required", "data": None}
    USER_PASSWORD_UPDATE_FAILED = {"code": 20000006, "msg": "User Password Update Failed", "data": None}
    USER_ID_IS_NOT_EXIST = {"code": 20000007, "msg": "User Id Not Exist", "data": None}
    USER_IS_EMPTY = {"code": 20000008, "msg": "User Is Required", "data": None},
    EMAIL_IS_REQUIRED = {"code": 20000009, "msg": "Email Is Required", "data": None}
    PASSWORD_IS_REQUIRED = {"code": 20000010, "msg": "Password Is Required", "data": None}
