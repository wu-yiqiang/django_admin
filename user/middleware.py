from django.utils.deprecation import MiddlewareMixin


class JwtAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list= ['/user/login']
        path = request.path
        if path not in white_list and path.startswith('/midia'):
            pass