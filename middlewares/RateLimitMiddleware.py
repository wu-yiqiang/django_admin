import time
from django.core.cache import cache



def rate_limit_by_user(request):
    user = request.user
    user_id = user.id if user.is_authenticated else 'anonymous'
    request_count_key = f'request_count:user:{user_id}'
    current_time = int(time.time())
    cache_key = f'request_time:user:{user_id}:{current_time // 60}'

    request_count = cache.get(request_count_key, 0)
    cache.add(cache_key, None, 60)
    cache.incr(request_count_key)

    if request_count >= 100:
        # 返回请求频率过高的错误响应
        return HttpResponseForbidden('请求频率过高，请稍后再试。')