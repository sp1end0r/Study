#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#file name : assign5.py
#짝짓기
import timeit
start = timeit.default_timer()
stop = timeit.default_timer()
print ("execute time : %f" %(stop - start))

def combination(data):
    remove_overlap = set(data)
    res = list(remove_overlap)
    length = len(res)
    for i in range (0, length-1):
        for j in range(i+1, length):
            print(res[j] + "-" + res[i])


if __name__ == "__main__":
    name1 = ["Tom", "Jerry", "Mike"]
    name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike", "Tom", "Jerry", "John"]
    start = timeit.default_timer()
    combination(name1)
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))

    print ()

    start = timeit.default_timer()
    combination(name2)
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))