#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:40:46 2019

@author: yaoxinzhi
"""

def main():
    country_list = []
    for i in range(5):
       country_list.append(input())
    country_list = sorted(country_list)
    print (country_list[0])

if __name__ == '__main__':
    main()