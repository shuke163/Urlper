#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2017/11/21

import hashlib


def md5(password):
    """
    密码字符串的md5值
    :param password: 密码字符串
    :return: 密码hash后的md5值
    """
    obj = hashlib.md5(b'AdsaKaLsixhansdxWdOdsapH')
    obj.update(password.encode('utf-8'))
    res = obj.hexdigest()
    return res
