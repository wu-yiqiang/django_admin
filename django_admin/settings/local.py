from .base import *

ALLOWED_HOSTS = ['*', ]
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
