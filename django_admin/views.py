from datetime import datetime
from django.views import View

from django_admin import settings
from common.response import ResponseSuccess, ResponseError
from service_error.common import COMMON_RERROR


class UploadView(View):
    def post(self, request):
        file = request.FILES.get('file')
        if file:
            file_name = file.name
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffixName
            file_path = str(settings.MEDIA_ROOT) + "/avatar/" + new_file_name
        try:
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            addr = settings.PROTOCOL + '://' + settings.IP + ':' + settings.PORT + '/media/avatar/' + new_file_name
            return ResponseSuccess(data=addr)
        except Exception as e:
            print("error", e)
            return ResponseError(COMMON_RERROR.FILE_UPLOAD_IS_FAILED)
