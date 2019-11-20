#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 재귀를 이용한 0부터 n까지의 합 
import timeit

def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num-1)


if __name__ == "__main__":
    start = timeit.default_timer()
    print ("%d" % sum_num(800))
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))