# -*- coding:utf-8 -*-
"""
@author: XiangNan
@desc: 
"""


class PoolEmptyException(Exception):
    def __str__(self):
        """
        proxypool is used out
        :return:
        """
        return repr('no proxy in proxypool')