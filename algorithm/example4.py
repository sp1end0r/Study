#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# filename : example4.py
# 선택정렬 
import timeit, random

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1): 
        min_idx = i
        for j in range(i + 1, n):
            if a[j] > a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    
    print (a)

myList = []
num = random.randrange(0, 1000)
for i in range(2) :
    while num in myList : # 중복될 경우
        num = random.randrange(0, 1000) # 다시 난수 생성
    myList.append(num) # 중복 되지 않은 경우만 추가

start = timeit.default_timer()
sel_sort(myList)
stop = timeit.default_timer()
print ("execute time : %f" %(stop - start))



