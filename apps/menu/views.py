import json
from code import interact
from sqlite3 import IntegrityError
from rest_framework.viewsets import ViewSet
from django.core.paginator import Paginator
from django.db import transaction
from django.views import View
from apps.menu.models import Menu, MenuSerializer, MenuTreeSerializer
from common.request import requestSerializer
from common.response import ResponseSuccess, ResponseError, ResponseSuccessPage
from common.validate import request_verify
from service_error.common import COMMON_RERROR
from service_error.menu import MENU_RERROR


class MenuViewSet(ViewSet):
    def list(self, request):
        pass

    def create(self, request):
        menuData = json.loads(request.body)
        try:
            with transaction.atomic():
                menu = Menu.objects.create(name=menuData['name'], icon="", parent_id=menuData['parent_id'],
                                           order_num=menuData['order_num'],
                                           menu_type=menuData['menu_type'], code=menuData['code'])
                print("新增", menu)
                menu.intefaces.add(*menuData['intefaces'])
                menu.buttons.add(*menuData['buttons'])
                return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    def destroy(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            Menu.objects.filter(id=menu_id).delete()
            return ResponseSuccess()
        except Exception as e:
            return ResponseError()

    def update(self, request):
        menuData = json.loads(request.body)
        id = menuData.get('id')
        try:
            with transaction.atomic():
                menu = Menu.objects.filter(id=id).update(name=menuData['name'], icon="",
                                                         parent_id=menuData['parent_id'],
                                                         order_num=menuData['order_num'],
                                                         menu_type=menuData['menu_type'], code=menuData['code'])
                menuobj = Menu.objects.get(id=id)
                menuobj.intefaces.set(menuData.get('intefaces'))
                menuobj.buttons.set(menuData.get('buttons'))
                return ResponseSuccess()
        except IntegrityError:
            return ResponseError()

    @request_verify('post', ['pageSize', 'pageNo'])
    def retrieve(self, request):
        params = requestSerializer(request.body)
        pageSize = params.get('pageSize')
        pageNo = params.get('pageNo')
        try:
            menus = Menu.objects.filter(is_deleted=0, name__icontains=params.get('search'))
            menuLists = MenuSerializer(Paginator(menus, pageSize).page(pageNo), many=True).data
            total = menus.count()
            return ResponseSuccessPage(data=menuLists, total=total, pageSize=pageSize, pageNo=pageNo)
        except Exception as e:
            return ResponseError()

    def details(self, request, menu_id):
        if menu_id is None:
            return ResponseError(MENU_RERROR.MENU_ID_IS_EMPTY)
        try:
            menu = Menu.objects.get(id=menu_id)
            menuinfo = MenuSerializer(menu).data
            return ResponseSuccess(data=menuinfo)
        except Exception as e:
            return ResponseError()

    def permissions(self, request, menu_id):
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

    def trees(self, request):
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
