#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# filename : example7.py

import random, timeit

def binary_search(a, x):
    # 탐색할 범위를 저장하는 변수 start, end
    # 리스트 전체를 범위로 탐색 시작(0 ~ len(a) -1)
    start = 0
    end = len(a) - 1
    while start <= end:            # 탐색할 범위가 남아 있는 동안 반복
        mid = (start + end) // 2   # 탐색 범위의 중간 위치
        if x == a[mid]:           # 발견!
            return mid
        elif x > a[mid]:           # 찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
            start = mid + 1
        else:                      # 찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 계속 탐색
            end = mid - 1
    return -1                      # 찾지 못했을 때
    
myList = []
num = random.randrange(0, 1000)
for i in range(800) :
    while num in myList : # 중복될 경우
        num = random.randrange(0, 1000) # 다시 난수 생성
    myList.append(num) # 중복 되지 않은 경우만 추가

start = timeit.default_timer()
binary_search(myList, num)
stop = timeit.default_timer()
print ("execute time : %f" %(stop - start))