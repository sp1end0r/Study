#/usr/local/bin/python3
# -*- coding: utf-8 -*-
def _quick_sort_sub(data, start, end, column):
    res = data
    if end - start <= 0:
        return
    pivot = res[end][column]   
    i = start
    for j in range(start, end):
        if res[j][column] <= pivot:

            res[i], res[j] = res[j], res[i]
            i += 1
    res[i], res[end] = res[end], res[i]
    _quick_sort_sub(res, start, i - 1, column) 
    _quick_sort_sub(res, i + 1, end, column)  

def rec_quick_sort(data, column):
    _quick_sort_sub(data, 0, len(data) - 1, column)

def _partition(res, start, end, column):
    pivot = res[start][0]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and res[left][column] <= pivot:
            left += 1
        while left <= right and res[right][column] > pivot:
            right -= 1
        if right < left:
            done = True
        else:
            res[left], res[right] = res[right], res[left]
    res[start], res[right] = res[right], res[start]  
    return right

def seq_quick_sort(data, column):
    res = data
    stack = []
    start = 0
    end = len(res)-1
    stack.append(start)
    stack.append(end)

    while stack:
        end = stack.pop()
        start = stack.pop()
        pivot = _partition(res, start, end, column)

        if int(pivot - 1) > start:
            stack.append(start)
            stack.append(pivot - 1)

        if int(pivot + 1) < end:
            stack.append(pivot + 1)
            stack.append(end)

    return res