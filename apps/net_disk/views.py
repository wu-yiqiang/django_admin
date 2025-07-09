import json
import os
from datetime import datetime
from django.views import View
from django_admin import settings
from common.response import ResponseSuccess, ResponseError
from service_error.common import COMMON_RERROR
from apps.net_disk.models import NetDisk, NetDiskSerializer


class UploadNetView(View):
    def post(self, request):
        file = request.FILES.get('file')
        if file:
            file_name = file.name
            file_size = file.size
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffixName
            file_path = str(settings.MEDIA_ROOT) + "/netdisk/" + new_file_name
        try:
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            NetDisk.objects.create(file_name=file_name, file_size=file_size, is_fold=False, parent_id=None)
            addr = getAddr(new_file_name)
            return ResponseSuccess(data=addr)
        except Exception as e:
            return ResponseError(COMMON_RERROR.FILE_UPLOAD_IS_FAILED)


class GetUploadView(View):
    def post(self, request):
        params = json.loads(request.body)
        id = params.get('id')
        net_disk_files = NetDisk.objects.filter(parent_id=id)
        net_disk_file_lists = NetDiskSerializer(net_disk_files.values(), many=True).data
        return ResponseSuccess(data=net_disk_file_lists)


class CreateFoldView(View):
    def post(self, request):
        params = json.loads(request.body)
        file_name = params.get('fileName')
        parent_id = params.get('parentId')
        is_fold = params.get('isFold')
        file_size = params.get('fileSize')
        NetDisk.objects.create(file_name=file_name, file_size=file_size, is_fold=is_fold, parent_id=parent_id)
        return ResponseSuccess()


class DeleteFilesView(View):
    def post(self, request):
        params = json.loads(request.body)
        files = params.get('files')
        NetDisk.objects.filter(id__in=files).delete()
        return ResponseSuccess()


class BatchUpdateView(View):
    def post(self, request):
        params = json.loads(request.body)
        ids = params.get('ids')
        parent_id = params.get('parent_id')
        NetDisk.objects.filter(id__in=ids).update(parent_id=parent_id)
        return ResponseSuccess()


class TreeListView(View):
    def buildTreeMenu(self, NetDiskList):
        resultNetDiskList: list[NetDiskList] = list()
        for netDisk in NetDiskList:
            for e in NetDiskList:
                if e.parent_id == netDisk.id:
                    if not hasattr(netDisk, "children"):
                        netDisk.children = list()
                    netDisk.children.append(e)
            if netDisk.parent_id is None:
                resultNetDiskList.append(netDisk)
        return resultNetDiskList

    def get(self, request):
        try:
            netDiskQuerySet = NetDisk.objects.order_by("id").filter(is_deleted=0, is_fold=True)
            NetDiskList: list[NetDisk] = self.buildTreeMenu(netDiskQuerySet)
            serializerNetDiskList: list[NetDiskSerializer] = list()
            if (NetDiskList):
                for netDisk in NetDiskList:
                    serializerNetDiskList.append(NetDiskSerializer(netDisk).data)
            return ResponseSuccess(data=serializerNetDiskList)
        except Exception as e:
            print("sssss", e)
            return ResponseError()


def getAddr(path: str) -> str:
    return settings.PROTOCOL + '://' + settings.IP + ':' + settings.PORT + '/storage/netdisk/' + path
