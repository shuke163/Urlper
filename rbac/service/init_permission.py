#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/20
from django.conf import settings
import json


def init_permission(request, user):
    """
    初始化，得到菜单列表及权限信息，写入session中
    :param user:
    :param request:
    :return:
    """
    # 去空去重
    permission_list = user.roles.filter(permissions__id__isnull=False).values('permissions__id',
                                                                              'permissions__title',     # 权限组标题
                                                                              'permissions__url',       # 权限URL
                                                                              'permissions__code',      # 权限码
                                                                              'permissions__menu_gp_id',# 组内菜单ID，Null表示是菜单选项
                                                                              'permissions__group_id',  # 权限的组ID
                                                                              'permissions__group__menu_id',      # 权限的组的菜单ID
                                                                              'permissions__group__menu__title',  # 权限的组的菜单标题
                                                                              ).distinct()

    # 菜单key
    menu_permission_list = []
    for item in permission_list:
        tpl = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url'],
            'menu_gp_id': item['permissions__menu_gp_id'],
            'menu_id': item['permissions__group__menu_id'],
            'menu_title': item['permissions__group__menu__title']
        }
        menu_permission_list.append(tpl)
    # List格式
    # print(json.dumps(menu_permission_list, indent=4, ensure_ascii=False))
    request.session[settings.PERMISSION_MENU_KEY] = menu_permission_list

    # 权限key，中间件使用
    result = {}
    for item in permission_list:
        group_id = item['permissions__group_id']
        code = item['permissions__code']
        url = item['permissions__url']
        if group_id in result:
            result[group_id]['codes'].append(code)
            result[group_id]['urls'].append(url)
        else:
            result[group_id] = {
                'codes': [code, ],
                'urls': [url, ]
            }
    # Dict格式
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    request.session[settings.PERMISSION_URL_DICT_KEY] = result




