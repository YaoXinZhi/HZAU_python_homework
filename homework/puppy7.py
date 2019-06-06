#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:03:15 2019

@author: yaoxinzhi
"""

def main():
    str_input = input()
    
    count_dic = {}
    for i in str_input:
        if not count_dic.get(i):
            count_dic[i] = 1
        else:
            count_dic[i] += 1
    
    keys = sorted(count_dic, key= lambda x:count_dic[x], reverse=True)
    
    max_count = count_dic[keys[0]]
    print_list = []
    for i in keys:
        if count_dic[i] == max_count:
            print_list.append(i)
            
    print_list = sorted(print_list)
    
    for i in print_list:
        print ('{0} {1}'.format(i, max_count))

if __name__ == '__main__':
    main()