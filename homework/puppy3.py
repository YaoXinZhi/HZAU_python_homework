#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:11:58 2019

@author: yaoxinzhi
"""

# 小黄同志的第三题

def isPhoneNum(chunk):
    try:
        a, b, c = chunk.split('-')
        if a.isdigit() and b.isdigit() and c.isdigit():
            return True
    except:
        return False

def ex_PhoneNum(message):
    for i in range(len(message)):
        chunk = message[i: i+13]
        if isPhoneNum(chunk):
            print ('Phone number found: '+chunk)
    print ('Done')

if __name__ == '__main__':
    message='Call me at 186-7123-4567 tomorrow. 027-8728-1235 is my office. '
    
    ex_PhoneNum(message)