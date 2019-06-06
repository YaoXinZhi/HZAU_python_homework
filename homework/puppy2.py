#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:50:03 2019

@author: yaoxinzhi
"""

def get_day(year, month):
    year = int(year)
    month = int(month)
    # 定义大小月 2月特殊
    b_month = set([1, 3, 5, 7, 8, 10, 12])
    s_month = set([4, 6, 9, 11])
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # 年份能够被4整除不能被100整除 或者 能够被400整除 的是闰年
        if month == 2:
            print ('29')
        else:
            if month in b_month:
                print ('31')
            elif month in s_month:
                print ('30')
    else:
        # 否则不是闰年
        if month == 2:
            print ('28')
        else:
            if month in b_month:
                print ('31')
            elif month in s_month:
                print ('30')
        
if __name__ == '__main__':
    _input = input()
    year, month = _input.strip().split(' ')
    get_day(year, month)