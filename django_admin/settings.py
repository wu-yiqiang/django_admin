import os
import sys
from datetime import timedelta
from pathlib import Path
import datetime
from socket import socket
from apps import user
from apps.user.apps import UserConfig

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
SECRET_KEY = 'django-insecure-&o+ozke2rp@q3k@5t$jyfbgo^f)h4td4)xc07c-5vjyqai)0v2'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = ["*", ]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "rest_framework_jwt",
    "drf_spectacular",
    "corsheaders",
    "apps.user.apps.UserConfig",
    "apps.role.apps.RoleConfig",
    "apps.menu.apps.MenuConfig",
    "apps.button.apps.ButtonsConfig",
    "apps.inteface.apps.IntefaceConfig",
    "apps.dictionary.apps.DictionaryConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # 必须放在common中间件之前
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "middlewares.JwtAuthMiddleware.JwtAuthMiddleware"
]

ROOT_URLCONF = 'django_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_admin.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True  # 指定所有域名IP都可以访问
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
CORS_ALLOW_METHODS = [
    "POST",
    "GET",
    "DELETE",
    "PATCH",
    "PUT"
]  # 允许请求的方法

MEDIA_ROOT = BASE_DIR / 'storage'
MEDIA_URL = 'storage/'
# redis token过期时间单位秒
CACHE_TOKEN_EXPIRE = 60 * 60 * 24

JWT_AUTH = {
    # user => payload
    'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',
    # payload => token
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',
    # token => payload
    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',
    # token过期时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=CACHE_TOKEN_EXPIRE),
    # token刷新的过期时间
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 反爬小措施前缀
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": 暂不设置密码,
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    }
}

ALLOWED_HOSTS = ['*', ]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'EAMS',
    'DESCRIPTION': '接口文档',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
LOGS_DIR = BASE_DIR / 'logs'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {},
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d:%(funcName)s]：%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s]：%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'debug.log'),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    },
    'time_handler': {
        'level': 'INFO',
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'filename': os.path.join(LOGS_DIR, "time.log"),
        'when': 'D',
        'interval': 1,
        'backupCount': 5,
        'formatter': 'standard',
        'encoding': 'utf-8',
    }
}

DEBUG = True
PROTOCOL = 'http'
IP = '192.168.1.222'
PORT = '8000'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_admin',
        "USER": 'root',
        "PASSWORD": 'root@root',
        "HOST": '127.0.0.1',
        "PORT": '3306',
    }
}

# DEBUG = False
# PROTOCOL = 'https'
# IP = '185.198.166.245'
# PORT = '8000'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_admin',
#         "USER": 'mydjango',
#         "PASSWORD": 'mydjango@mydjango',
#         "HOST": '127.0.0.1',
#         "PORT": '3306',
#     }
# }
