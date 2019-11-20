#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# filename : example5.py
# 삽입 정렬
import timeit, random

def ins_sort(a):
    n = len(a)
    for i in range(1, n): 
        key = a[i]
        j = i - 1
       
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j] 
            j -= 1
        a[j + 1] = key
        print (a)

myList = []
num = random.randrange(0, 1000)
for i in range(800) :
    while num in myList : # 중복될 경우
        num = random.randrange(0, 1000) # 다시 난수 생성
    myList.append(num) # 중복 되지 않은 경우만 추가

start = timeit.default_timer()
ins_sort(myList)
stop = timeit.default_timer()
print ("execute time : %f" %(stop - start))
