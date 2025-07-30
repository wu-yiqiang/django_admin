class COMMON_RERROR:
    SERVICE_ERROR = {"code": 10000000, "msg": "System Error", "data": None}
    DATA_PARSE_ERROR = {"code": 10000001, "msg": "Data Parse Error", "data": None}
    TOKEN_EXPIRED = {"code": 10000002, "msg": "Token Expired", "data": None}
    TOKEN_VERIFICATION_FAILED = {"code": 10000003, "msg": "Token Verification Failed", "data": None}
    TOKEN_VERIFICATION_EXCEPTION = {"code": 10000004, "msg": "Token Verification Exception", "data": None}
    PAGENATE_PARAMS_IS_EMPTY = {"code": 10000005, "msg": "Pagenate Params Is Empty", "data": None}
    FILE_UPLOAD_IS_FAILED = {"code": 10000006, "msg": "File Upload Failed", "data": None}
    ID_IS_EMPTY = {"code": 10000007, "msg": "Query ID Is Empty", "data": None}
    IS_NOT_AUTH = {"code": 10000008, "msg": "The interface is not authorized.", "data": None}
    REQUEST_METHOD_ERROR = {"code": 10000009, "msg": "The request method is error.", "data": None}
    PARAMS_IS_NULL = {"code": 10000010, "msg": "The params is null.", "data": None}
    PARAM_IS_NULL = {"code": 10000011, "msg": " is required.", "data": None}
    SERVICE_BUSY = {"code": 10000012, "msg": "service is busy,please try again later.", "data": None}


# @Desc: { 项目响应码模块 }
class USER_RERROR:
    USER_IS_NOT_EXIST = {"code": 20000001, "msg": "user is not exist", "data": None}
    EMAIL_OR_PASSWORD_ERROR = {"code": 20000002, "msg": "email or password error", "data": None}
    USER_AND_PASSWORD_IS_REQUIRED = {"code": 20000003, "msg": "user and password is Required", "data": None}
    USERNAME_IS_EMPTY = {"code": 20000004, "msg": "Username Is Required", "data": None}
    PASSWORD_IS_EMPTY = {"code": 20000005, "msg": "Password Is Required", "data": None}
    USER_PASSWORD_UPDATE_FAILED = {"code": 20000006, "msg": "User Password Update Failed", "data": None}
    USER_ID_IS_NOT_EXIST = {"code": 20000007, "msg": "User Id Not Exist", "data": None}
    USER_IS_EMPTY = {"code": 20000008, "msg": "User Is Required", "data": None}
    EMAIL_IS_REQUIRED = {"code": 20000009, "msg": "Email Is Required", "data": None}
    PASSWORD_IS_REQUIRED = {"code": 20000010, "msg": "Password Is Required", "data": None}


class ROLE_RERROR:
    ROLE_IS_NOT_EXIST = {"code": 30000001, "msg": "role is not exist", "data": None}
    ROLE_NAME_IS_EMPTY = {"code": 30000002, "msg": "RoleName Is Empty", "data": None}
    ROLE_INFO_UPDATE_FAILED = {"code": 30000003, "msg": "Role Info Update Failed", "data": None}
    ROLE_ID_IS_NOT_EXIST = {"code": 30000004, "msg": "Role Id Not Exist", "data": None}


# @Desc: { 项目响应码模块 }
class MENU_RERROR:
    MENU_IS_NOT_EXIST = {"code": 40000001, "msg": "Menu Is Not Exist", "data": None}
    MENU_ID_IS_EMPTY = {"code": 40000002, "msg": "Menu ID Is Empty", "data": None}
