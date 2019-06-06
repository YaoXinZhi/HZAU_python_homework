#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:43:56 2019

@author: yaoxinzhi
"""

def main():
    int_num = int(input())
    if int_num not in range(1, 101):
        print ('The number of integers is out of range')
        
    num_str = input()
    int_list = [int(i) for i in num_str.split()]
    int_dic = {}
    for i in int_list:
        if not int_dic.get(i):
            int_dic[i] = 1
        else:
            int_dic[i] += 1
            
    keys = sorted(int_dic, key=lambda x:int_dic[x], reverse=True)
    
    print_list = []
    max_count = int_dic[keys[0]]
    for i in keys:
        if int_dic[i] == max_count:
            print_list.append(i)
            
    print_list = sorted(print_list)
    
    for i in print_list:
        print ('{0} {1}'.format(i, max_count))
    

if __name__ == '__main__':
    main()