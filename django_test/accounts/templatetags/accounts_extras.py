# -*- coding: utf-8 -*-
# @Time : 2021/11/30 10:54 下午
# @Author : mac
# @Email : 692653284@qq.com
# @File : accounts_extras.py
# @Project : django_test
import locale
from decimal import Decimal

from django import template

register = template.Library()


def warning(value):
    if value:
        return '<span class="red">' + value[0] + '</span>' + value[1:]
    else:
        return value


register.filter('warning', warning)


# 金额过滤器 1,000.00
def money(value):
    value = '{:.2f}'.format(value)
    list_money = list(str(value))
    list_money.reverse()
    j = 0
    for i in range(len(list_money)):
        if (i-3) > 0 and (i-3) % 3 == 0:
            list_money.insert(i + j, ',')
            j += 1
    list_money.reverse()
    final_money = "".join(list_money)
    return final_money


register.filter("money", money)


# 第二种方法
def accounting(value, place=2):
    try:
        place = int(place)
    except Exception as e:
        print(e)
        place = 2

    try:
        value = Decimal(value)
        locale.setlocale(locale.LC_ALL, '')
        return locale.format_string('%.*f', (place, value), True)
    except Exception as e:
        print(e)
        return value


register.filter("accounting", accounting)


if __name__ == '__main__':
    print(accounting(100000000000000.3333))