#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 0부터 n까지의 합
import timeit

def sum(num): 
    res = 0
    start = timeit.default_timer()
    for num in range (1,num+1):
        res = res+(num*num)
        print ("calulating %d times.." % num)
    
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))
    return res


if __name__ == "__main__":
    try:
        num = int(input("input your natural number >> "))
        if num <= 0 : # checking natural number 
            print ("Please input natural number ..")
        else : 
            res = int(sum(num))
            print ("sum of value from 1 to %d is %d" % (num, res) )
    
    except ValueError:
        print ("ValueError : wrong number ..")

