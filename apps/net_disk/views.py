import json
import os
import uuid
from rest_framework.viewsets import ViewSet
from django.views import View
from django_admin import settings
from common.response import ResponseSuccess, ResponseError
from common.errors import COMMON_RERROR
from apps.net_disk.models import NetDisk, NetDiskSerializer


def getAddr(path: str) -> str:
    return settings.PROTOCOL + '://' + settings.IP + ':' + settings.PORT + '/storage/netdisk/' + path


class NetDiskViewSet(ViewSet):
    def upload(self, request):
        file = request.FILES.get('file')
        parent_id = request.POST.get('parent_id')
        if file:
            file_name = file.name
            file_size = file.size
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = str(uuid.uuid4()) + suffixName
            file_path = str(settings.MEDIA_ROOT) + "/netdisk/" + new_file_name
        try:
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            NetDisk.objects.create(file_name=file_name, url=new_file_name, file_size=file_size, is_fold=False,
                                   parent_id=parent_id)
            return ResponseSuccess()
        except Exception as e:
            print("file upload error", e)
            return ResponseError(COMMON_RERROR.FILE_UPLOAD_IS_FAILED)

    def current_files(self, request):
        params = json.loads(request.body)
        id = params.get('id')
        net_disk_files = NetDisk.objects.filter(parent_id=id)
        net_disk_file_lists = NetDiskSerializer(net_disk_files.values(), many=True).data
        return ResponseSuccess(data=net_disk_file_lists)

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

    def tree_list(self, request):
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

    def batch_update(self, request):
        params = json.loads(request.body)
        ids = params.get('ids')
        parent_id = params.get('parent_id')
        NetDisk.objects.filter(id__in=ids).update(parent_id=parent_id)
        return ResponseSuccess()

    def create_fold(self, request):
        params = json.loads(request.body)
        file_name = params.get('file_name')
        parent_id = params.get('parent_id')
        file_size = params.get('file_size')
        NetDisk.objects.create(file_name=file_name, file_size=file_size, is_fold=True, parent_id=parent_id)
        return ResponseSuccess()

    def delete(self, request):
        params = json.loads(request.body)
        fileIds = params.get('files')
        deleteIds = fileIds
        # 查询所有父ID为该ID的数据
        for fileId in fileIds:
            parentIds = NetDisk.objects.filter(parent_id=fileId)
            parent_id = parentIds.values_list('id', flat=True)
            deleteIds.extend(parent_id)
        for id in deleteIds:
            file = NetDisk.objects.filter(id=id).first()
            file.delete()
            if file.is_fold is False:
                path = str(settings.MEDIA_ROOT) + "/netdisk/" + file.url
                if os.path.exists(path):
                    os.remove(path)
        return ResponseSuccess()
