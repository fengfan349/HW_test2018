# -*- coding:utf-8 -*-
# python3
import sys
import os
originStr = []
temp = []
k = 0
len_temp = 1
originStr = sorted(list(input()))
out_str = []
#print(originStr)
while (len(originStr) > 0):
    for word in originStr :
        #print(word)
        if word not in temp:
            temp.append(word)
    for i in range(len(temp)):
        originStr.pop(originStr.index(temp[i]))
        out_str.append(temp[i])
    temp = []
    #originStr = sorted(originStr)
    #print(originStr,''.join(temp))
    #print(temp,len_temp)
#print(temp)
print(''.join(out_str))