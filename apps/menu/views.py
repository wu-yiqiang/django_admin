import json

from django.core.paginator import Paginator
from django.views import View
from apps.menu.models import Menu, MenuSerializer
from common.response import ResponseSuccess, ResponseError
from service_error.common import COMMON_RERROR
from service_error.menu import MENU_RERROR


class CreateView(View):
    def post(self, request):
        menu = json.loads(request.body)
        Menu.objects.create(name=menu['name'], icon="", parent_id=menu['parent_id'],
                            path=menu['path'], order_num=menu['order_num'],
                            menu_type=menu['menu_type'], code=menu['code'])
        return ResponseSuccess()


class TreeListView(View):
    # 构造菜单树
    def buildTreeMenu(self, MenuList):
        resultMenuList: list[Menu] = list()
        for menu in MenuList:
            # 寻找子节点
            for e in MenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            # 判断父节点，添加到集合
            if menu.parent_id is None:
                resultMenuList.append(menu)
        return resultMenuList

    def get(self, request):
        menuQuerySet = Menu.objects.order_by("order_num").filter(is_deleted=0)
        # 构造菜单树
        MenuList: list[Menu] = self.buildTreeMenu(menuQuerySet)
        serializerMenuList: list[MenuSerializer] = list()
        if MenuList is None:
            return ResponseSuccess(data=[])
        for Menu in MenuList:
            serializerMenuList.append(MenuSerializer(Menu).data)
        return ResponseSuccess(data=serializerMenuList)


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        roleLists = Paginator(Menu.objects.filter(is_deleted=0), pageSize).page(pageNo)
        total = Menu.objects.filter(is_deleted=0).count()
        roles = MenuSerializer(roleLists.object_list.values(), many=True).data
        data = {'lists': roles, 'total': total, 'pageSize': pageSize, 'pageNo': pageNo}
        return ResponseSuccess(data=data)


class UpdateView(View):
    def post(self, request):
        menu = json.loads(request.body)
        id = menu.get('id')
        menu = Menu.objects.filter(id=id).update(name=menu['name'], icon="", parent_id=menu['parent_id'],
                                                 # path=menu['path'],
                                                 order_num=menu['order_num'],
                                                 menu_type=menu['menu_type'], code=menu['code'])
        return ResponseSuccess()


class DetailView(View):
    def get(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        menu = Menu.objects.get(id=menu_id)
        menuinfo = MenuSerializer(menu).data
        return ResponseSuccess(data=menuinfo)


class DeleteView(View):
    def delete(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        # role = Menu.objects.get(id=menu_id)
        # role.is_deleted = 1
        # role.save()
        Menu.objects.filter(id=menu_id).delete()
        return ResponseSuccess()
