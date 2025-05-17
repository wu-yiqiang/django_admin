from .base import *

ALLOWED_HOSTS = ['127.0.0.1']
DEBUG = False
PROTOCOL = 'https'
IP = '185.198.166.245'
PORT = '8000'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_admin',
        "USER": 'mydjango',
        "PASSWORD": 'mydjango@mydjango',
        "HOST": '127.0.0.1',
        "PORT": '3306',
    }
}
