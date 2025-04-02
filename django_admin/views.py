from datetime import datetime
from django.views import View

from django_admin import settings
from common.response import ResponseSuccess, ResponseError
from service_error.common import COMMON_RERROR


class UploadView(View):
    def post(self, request):
        file = request.FILES.get('avatar')
        print("file:", file)
        if file:
            file_name = file.name
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffixName
            file_path = str(settings.MEDIA_ROOT) + "\\userAvatar\\" + new_file_name
            print("file_path:", file_path)
        try:
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            return ResponseSuccess(data=new_file_name)
        except:
            return ResponseError(COMMON_RERROR.FILE_UPLOAD_IS_FAILED)
