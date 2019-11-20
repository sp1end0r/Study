#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def heap_sort(data, row):
    res = data
    length = len(res)
    res = [0]+res

    for i in range(length, 0, -1):
        _heapify(res, i , length,row)

    for i in range(length, 0 , -1):
        res[i], res[1] = res[1], res[i]
        _heapify(res, 1, i-1, row)
    del res[0]
    return res




def _heapify(data, idx, length, row):
    left = idx*2
    right = idx*2+1
    current = idx

    if(left <= length and data[current][row] < data[left][row]):
        current = left
    
    if(right <= length and data[current][row] < data[right][row]):
        current = right
    
    if current != idx:
        data[idx], data[current] = data[current], data[idx]
        return _heapify(data, current, length,row)
