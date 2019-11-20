#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 최대값과 최소값을 찾는 함수
import timeit
import random

def find_max(data):
    length = len(data)
    max_data = data[0]
    try : 
        start = timeit.default_timer()
        for i in range (1, length):
            if data[i] > max_data:
                max_data = data[i]
        stop = timeit.default_timer()
        print ("execute time : %f" %(stop - start))
        return max_data

    except UnboundLocalError:
        print ("FindMaxData : UnboundLocalError : A few data ..")
        exit(0)

def find_min(data):
    length = len(data)
    min_data = data[0]
    try :
        for i in range(1, length):
            if data[i] < min_data:
                min_data = data[i]
        return min_data

    except UnboundLocalError:
        print ("FindMinData : UnboundLocalError : A few data ..")
        exit(0)

def input_interface():
    try : 
        data = list(map(float, input("input your number >>").split(" ")))
        return data

    except ValueError:
        print("ValueError : pleses input number ...")
        return

def menu(data):
    print ("============================")
    print ("         Select contents")
    print ("============================")
    print ("1. Input data in List")
    print ("2. Find Maximum data in List")
    print ("3. Find Minimum data in List")
    print ("0. Exit ")
    print ("============================")
    if not data : 
        print ("List is empty!")
    else : 
        print (data)
    print ("============================")
    try : 
        res = int(input(">> "))
        return res
    
    except ValueError : 
        print ("Error invaild value..")
        return 

if __name__ == "__main__":
    myList = []

    num = random.randrange(0, 1000)



    for i in range(800) :

        while num in myList : # 중복될 경우

            num = random.randrange(0, 1000) # 다시 난수 생성

        myList.append(num) # 중복 되지 않은 경우만 추가

    print(myList)
    find_max(myList)

