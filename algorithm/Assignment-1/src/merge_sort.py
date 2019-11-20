#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def rec_merge_sort(data, row):
    length = len(data)
    if length<=1 :
            return
    mid = length//2
    g1 = data[:mid]
    g2 = data[mid:]

    rec_merge_sort(g1, row)
    rec_merge_sort(g2, row)

    i1 = 0
    i2 = 0 
    ia = 0
    while i1 < len(g1) and i2 <len(g2):
        if g1[i1][row] < g2[i2][row]:
            data[ia] = g1[i1]
            i1 += 1
            ia += 1
        else :
            data[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1):
        data[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        data[ia] = g2[i2]
        i2 += 1
        ia += 1

def seq_merge_sort(data, row):
    res = data
    right = 0; wid = 0; rend = 0; left = 0
    k = 1

    num = len(res)
    temp = [0] * num

    while(k < num):
        left = 0
        while(left + k < num):
            right = left + k
            rend = right + k
            if(rend > num):
                rend = num
            m = left; i = left; j = right

            while(i < right and j < rend):
                if res[i][row] <= res[j][row]:
                    temp[m] = res[i]
                    i += 1
                else:
                    temp[m] = res[j]
                    j += 1
                m += 1

            while(i < right):
                temp[m] = res[i]
                i += 1; m += 1
            while(j < rend):
                temp[m] = res[j]
                j += 1; m += 1
            m = left
            while(m < rend):
                res[m] = temp[m]
                m += 1
            left += k * 2
        k *= 2
        
    return res