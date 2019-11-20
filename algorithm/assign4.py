#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#file name : assign4.py
# 같은 데이터 찾기
import timeit
import random


def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])


    if not result :
        print("no over lap in list !")
    else : 
        print ("the same name in list : %s" % result)
        n2 = len(result)
        res = list(result)
        for i in range(0,n2):
            count = 0
            for j in range (0, n):
                if res[i] == a[j]:
                    count = count + 1
            print (res[i] + "'s numbers in list : %d" % count)
    

if __name__ == "__main__":
    myList = []

    num = random.randrange(0, 1000)



    for i in range(800) :

        while num in myList : # 중복될 경우

            num = random.randrange(0, 1000) # 다시 난수 생성

        myList.append(num) # 중복 되지 않은 경우만 추가

    print(myList)
    start = timeit.default_timer()
    find_same_name(myList)
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))
