import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.cache import cache
from django_admin import settings


def set_cache(key, data, timeout=settings.CACHE_TOKEN_EXPIRE):
    cache.set(key, json.dumps(data, cls=DjangoJSONEncoder), timeout)


def get_cache(key):
    if cache.has_key(key) is False:
        return None
    cache_data = cache.get(key)
    return json.loads(cache_data)
