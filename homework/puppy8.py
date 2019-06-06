#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:07:35 2019

@author: yaoxinzhi
"""

def main():
    
    num_list = []
    for i in range(3):
        num_list.append(float(input()))
    
    abs_dic = {}
    for i in num_list:
        abs_dic[i] = abs(i)
    
    keys = sorted(num_list, key= lambda x:abs_dic[x], reverse=False)
    
    min_abs = abs_dic[keys[0]]
    print_list = []
    for i in keys:
        if abs_dic[i] == min_abs:
            print_list.append(i)
    
    print_str = ''
    for i in print_list:
        print_str += str(i)
        print_str += ' '
    print(print_str)
    
if __name__ == '__main__':
    main()