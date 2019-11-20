#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# filename : example3.py
#순차탐색
import timeit, random

def search_list(a, x):
    n = len(a)  
    res = []            
    for i in range(0, n):   
        if x == a[i]:      
            res.append(i)    
    return res    
 

myList = []
num = random.randrange(0, 1000)
for i in range(800) :
    while num in myList : # 중복될 경우
        num = random.randrange(0, 1000) # 다시 난수 생성
    myList.append(num) # 중복 되지 않은 경우만 추가

print(myList)
start = timeit.default_timer()
search_list(myList, num)
stop = timeit.default_timer()
print ("execute time : %f" %(stop - start))
