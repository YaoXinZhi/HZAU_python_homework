#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:36:32 2019

@author: yaoxinzhi
"""

def main():
    PhoneBook = {'mayun':'13309283335',

    'zhaolong':'18989227822',

    'zhangmin':'13382398921',

    'Gorge':'19833824743',

    'Jordan':'18807317878',

    'Curry':'15093488129',

    'Wade':'19282937665'}
    
    search_name = input()
    if not PhoneBook.get(search_name):
        print ('not found')
    else:
        print (PhoneBook[search_name])
    
if __name__ == '__main__':
    main()