#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def select_sort(data, row):
    res = data
    length = len(res)
    for i in range(0, length - 1): 
        min_idx = i
        for j in range(i + 1, length):
            if res[j][row] < res[min_idx][row]:
                min_idx = j
        res[i], res[min_idx] = res[min_idx], res[i]
    
    return res