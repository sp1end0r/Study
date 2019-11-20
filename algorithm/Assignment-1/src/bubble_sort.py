#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def bubble_sort(data, column):
    res = data
    length = len(res)
    for i in range (length-1):
        for j in range(length-i-1):
            
            if res[j][column] > res[j+1][column]:
                res[j], res[j+1] = res[j+1], res[j]
    
    return res

