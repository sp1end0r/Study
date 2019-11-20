#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#file name : assign6.py
# 피보나치 수열
import timeit

def sum_number(data):
    if data == 1 : return 1

    return data + sum_number(data-1)

def compare_number(num1, num2):
    if num1 >= num2 :
        return  num1
    else : 
        return num2

def find_max(data, length):
    if length == 1:
        return data[0]
    else : 
          return compare_number(data[length-1],find_max(data, length-1))
          
def fibonacci(num):
    if num < 2:
        return num
    else :
        return fibonacci(num-1) + fibonacci(num-2)


if __name__ == "__main__":
    data3 = 50
    start = timeit.default_timer()
    fibonacci(data3)
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))
        