import json
from sqlite3 import IntegrityError

from django.core.paginator import Paginator
from django.db import transaction
from django.views import View
from apps.menu.models import Menu, MenuSerializer, MenuTreeSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage
from service_error.common import COMMON_RERROR
from service_error.menu import MENU_RERROR


class CreateView(View):
    def post(self, request):
        menu = json.loads(request.body)
        try:
            Menu.objects.create(name=menu['name'], icon="", parent_id=menu['parent_id'], order_num=menu['order_num'],
                                menu_type=menu['menu_type'], code=menu['code'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()


class TreeListView(View):
    def buildTreeMenu(self, MenuList):
        resultMenuList: list[Menu] = list()
        for menu in MenuList:
            print("menu", menu.id)
            for e in MenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            if menu.parent_id is None:
                resultMenuList.append(menu)
        return resultMenuList

    def get(self, request):
        try:
            menuQuerySet = Menu.objects.order_by("order_num").filter(is_deleted=0)
            MenuList: list[Menu] = self.buildTreeMenu(menuQuerySet)
            serializerMenuList: list[MenuTreeSerializer] = list()
            if (MenuList):
                for menu in MenuList:
                    serializerMenuList.append(MenuTreeSerializer(menu).data)
            return ResponseSuccess(data=serializerMenuList)
        except Exception as e:
            return ResponseError()


class SearchPageView(View):
    def post(self, request):
        params = json.loads(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        if not all([pageSize, pageNo]):
            return ResponseError(COMMON_RERROR.PAGENATE_PARAMS_IS_EMPTY)
        try:
            menus = Menu.objects.filter(is_deleted=0)
            menuLists = MenuSerializer(Paginator(menus, pageSize).page(pageNo), many=True).data
            total = menus.count()
            return ResponseSuccessPage(data=menuLists, total=total, pageSize=pageSize, pageNo=pageNo)
        except Exception as e:
            return ResponseError()


class UpdateView(View):
    def post(self, request):
        menu = json.loads(request.body)
        id = menu.get('id')
        try:
            Menu.objects.filter(id=id).update(name=menu['name'], icon="", parent_id=menu['parent_id'],
                                              order_num=menu['order_num'],
                                              menu_type=menu['menu_type'], code=menu['code'])
            return ResponseSuccess()
        except IntegrityError:
            return ResponseError()


class DetailView(View):
    def get(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            menu = Menu.objects.get(id=menu_id)
            menuinfo = MenuSerializer(menu).data
            return ResponseSuccess(data=menuinfo)
        except Exception as e:
            return ResponseError()


class DeleteView(View):
    def delete(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            Menu.objects.filter(id=menu_id).delete()
            return ResponseSuccess()
        except Exception as e:
            return ResponseError()


class SetMenuPermission(View):
    def put(self, request, menu_id):
        menuData = json.loads(request.body)
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            Menu.objects.filter(id=menu_id).delete()
            with transaction.atomic():
                menu = Menu.objects.filter(id=menu_id)
                menu.buttons.set(menuData.get('buttons'))
                menu.intefaces.set(menuData.get('intefaces'))
            return ResponseSuccess()
        except Exception as e:
            return ResponseError()


class MenuPermissionDetailView(View):
    def get(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            menu = Menu.objects.get(id=menu_id)
            menuinfo = MenuSerializer(menu).data
            return ResponseSuccess(data=menuinfo)
        except Exception as e:
            return ResponseError()
