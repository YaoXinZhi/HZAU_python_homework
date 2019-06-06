#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:57:25 2019

@author: yaoxinzhi
"""

def main(target):
    
    while True:
        guess = int(input())
        if guess == target:
            print ('you win')
            break
        if guess > target:
            print ('larger than expected')
        if guess < target:
            print ('less than expected')
    

if __name__ == '__main__':
    
    target = 100
    main(target)