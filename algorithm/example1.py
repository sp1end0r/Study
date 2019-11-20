#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 0부터 n까지의 합
import timeit

def sum(num): 
    return num*(num+1) // 2


if __name__ == "__main__":
    try:
        num = int(input("input your natural number >> "))
        if num <= 0 : # checking natural number 
            print ("Please input natural number ..")
        else : 
            start = timeit.default_timer()
            res = int(sum(num))
            stop = timeit.default_timer()
            print ("execute time : %f" %(stop - start))
            print ("sum of value from 1 to %d is %d" % (num, res) )
    
    except ValueError:
        print ("ValueError : wrong number ..")

