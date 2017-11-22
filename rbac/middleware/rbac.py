#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/20

from django.shortcuts import redirect, HttpResponse
from django.conf import settings
import re


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):
    """
    rbac中间件
    针对当前请求URL进行权限过滤

    """

    def process_request(self, request):
        current_url = request.path_info
        # 白名单URL
        for url in settings.VALID_URL:
            if re.match(url, current_url):
                return None
        # 当前用户的session中没权限字典，则返回登陆页面
        permission_dict = request.session.get(settings.PERMISSION_URL_DICT_KEY)
        if not permission_dict:
            return redirect(settings.LOGNIN_URL)

        flag = False
        for group_id, code_url in permission_dict.items():
            for db_url in code_url['urls']:
                regax = "^{0}$".format(db_url)
                # 获取当前用户对当前组内的所有code，并赋值给request对象，作为属性
                if re.match(regax, current_url):
                    request.permission_code_list = code_url['codes']
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return HttpResponse("无访问权限")
