#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def sum(num): 
    res = 0
    for num in range (1,num+1):
        res = res+(num*num)
        print ("calulating %d times.." % num)
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

