#!/bin/python3

import math
import os
import random
import re
import sys

def sortTheString(s):
    s_list = sorted(s)
    s_dict = dict()
    number = 0
    for alphabet in s_list:
        if s_dict.get(alphabet) is None:
            number = 1
            s_dict.update({alphabet:number})
        else:
            number+=1
            s_dict.update({alphabet:number})
    return s_dict

#{a:2, key, value}
def sortTheDict(s_dict):
    sorted_s_dict = {alpha:number for alpha, number in sorted(s_dict.items(), key=lambda item:item[1], reverse=True)}
    firstAlpha=''
    secondAlpha=''
    thirdAlpha=''
    firstNum=0
    secondNum=0
    thirdNum=0
    count = 1
    for alpha in sorted_s_dict.keys():
        if count == 1:
            firstAlpha = alpha
            firstNum = sorted_s_dict.get(alpha)
        elif count == 2:
            secondAlpha = alpha
            secondNum = sorted_s_dict.get(alpha)
        elif count == 3:
            thirdAlpha = alpha
            thirdNum = sorted_s_dict.get(alpha)
        else:
            break
        count+=1
        
    if firstNum == secondNum:
        if secondAlpha < firstAlpha:
            print(secondAlpha, secondNum)
        else:
            print(firstAlpha, firstNum)
    else:
        print(firstAlpha, firstNum)
          
    if secondNum == thirdNum:
        if thirdAlpha < secondAlpha:
            print(thirdAlpha, thirdNum)
            print(secondAlpha, secondNum)
        else:
            print(secondAlpha, secondNum)
            print(thirdAlpha, thirdNum)
    else:
        print(secondAlpha, secondNum)
        print(thirdAlpha, thirdNum)
    
if __name__ == '__main__':
    s = input()
    s_dict = sortTheString(s)
    sortTheDict(s_dict)