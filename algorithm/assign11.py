#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# file name : assign11.py
# Sequence Search using Dictionary
import timeit

def seq_serach(data, stu_no):
    for key in data :
        if key == stu_no: return data[key]   

    return "?"

if __name__ == "__main__":
    #data = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}
    data = {1:"hello", 2:"world", 3:"python",4:"python2",5:"python3", 6:"programming", 7:"coding", 8:"Hi",9:"bye"}
    #print (seq_serach(data, 14))
    #print (seq_serach(data, 15))
    start = timeit.default_timer()
    print (seq_serach(data,4))
    stop = timeit.default_timer()
    print ("execute time : %f" %(stop - start))



    




