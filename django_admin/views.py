import json
import os
import random
from datetime import datetime
from django.views import View
import time
from django_admin import settings
from common.response import ResponseSuccess, ResponseError
from common.errors import COMMON_RERROR
from django.http import HttpResponse
from django.http import StreamingHttpResponse


class UploadView(View):
    def post(self, request):
        file = request.FILES.get('file')
        if file:
            file_name = file.name
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffixName
            file_path = str(settings.MEDIA_ROOT) + "/avatar/" + new_file_name
        try:
            print("sss", file)
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            addr = settings.PROTOCOL + '://' + settings.IP + ':' + settings.PORT + '/storage/avatar/' + new_file_name
            return ResponseSuccess(data=addr)
        except Exception as e:
            print("error", e)
            return ResponseError(COMMON_RERROR.FILE_UPLOAD_IS_FAILED)


class UploadNetView(View):
    def post(self, request):
        file = request.FILES.get('file')
        if file:
            file_name = file.name
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffixName
            file_path = str(settings.MEDIA_ROOT) + "/netdisk/" + new_file_name
        try:
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            addr = settings.PROTOCOL + '://' + settings.IP + ':' + settings.PORT + '/storage/netdisk/' + new_file_name
            return ResponseSuccess(data=addr)
        except Exception as e:
            return ResponseError(COMMON_RERROR.FILE_UPLOAD_IS_FAILED)


class GetUploadView(View):
    def post(self, request):
        params = json.loads(request.body)
        path = params.get('path')
        file_path = f'{str(settings.MEDIA_ROOT)}{path}'
        files = os.listdir(file_path)
        files = []
        # fileStru = {
        #     id: 1,
        #     url: 'http://192.168.1.222:8000/storage/netdisk/2022_PDF.pdf',
        #     fileName: '2022_PDF.pdf',
        #     isFold: false,
        #     fileSize: '120kb'
        # },
        # for file in files:
        #     print(file)
        #     if os.path.isfile(f'{file_path}/{file}'):
        #         files.append(entry)
        #     elif os.path.isdir(f'{file_path}/{file}'):
        #         files.append(entry)
        # print("get", path, file_path)
        return ResponseSuccess()


def event_stream():
    while True:
        yield f"data: {random.randint(0, 130)}\n\n"
        time.sleep(settings.SSESENDINTERVAL)


class SSEView(View):

    def get(self, request):
        response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        return response
