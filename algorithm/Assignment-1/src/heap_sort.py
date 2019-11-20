#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def heap_sort(data, column):
    res = data
    length = len(res)
    res = [0]+res

    for i in range(length, 0, -1):
        _heapify(res, i , length,column)

    for i in range(length, 0 , -1):
        res[i], res[1] = res[1], res[i]
        _heapify(res, 1, i-1, column)
    del res[0]
    return res




def _heapify(data, idx, length, column):
    left = idx*2
    right = idx*2+1
    current = idx

    if(left <= length and data[current][column] < data[left][column]):
        current = left
    
    if(right <= length and data[current][column] < data[right][column]):
        current = right
    
    if current != idx:
        data[idx], data[current] = data[current], data[idx]
        return _heapify(data, current, length,column)
