#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# filename : example6.py
import timeit, random

def merge_sort(data):
    length = len(data)
    if length<=1 :
            return
    mid = length//2
    g1 = data[:mid]
    g2 = data[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0 
    ia = 0
    while i1 < len(g1) and i2 <len(g2):
        if g1[i1] < g2[i2]:
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
myList = []
num = random.randrange(0, 1000)
for i in range(800) :
    while num in myList : # 중복될 경우
        num = random.randrange(0, 1000) # 다시 난수 생성
    myList.append(num) # 중복 되지 않은 경우만 추가

start = timeit.default_timer()
merge_sort(myList)
stop = timeit.default_timer()
print (myList)
print ("execute time : %f" %(stop - start))
#if __name__ == "__main__":
#    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
#    print (d)
#    print("sorting .... done!")
#    merge_sort(d)
#
#    print(d)