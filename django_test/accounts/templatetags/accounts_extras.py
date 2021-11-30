# -*- coding: utf-8 -*-
# @Time : 2021/11/30 10:54 下午
# @Author : mac
# @Email : 692653284@qq.com
# @File : accounts_extras.py
# @Project : django_test
from django import template

register = template.Library()


def warning(value):
    if value:
        return '<span class="red">' + value[0] + '</span>' + value[1:]
    else:
        return value


register.filter('warning', warning)

# 金额过滤器 1,000.00
# TODO
