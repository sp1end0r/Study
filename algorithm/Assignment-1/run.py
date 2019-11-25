#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from src.bubble_sort import *
from src.heap_sort import *
from src.insert_sort import *
from src.merge_sort import *
from src.quick_sort import *
from src.select_sort import *
from src.load_data import *
from src.out_data import *
from src.interface import *
from src.listdir import *
import timeit


if __name__ =="__main__":
    path = os.getcwd()
    file_name = list_dir(path)
    orignal, field=load_data(path, file_name)
    data = orignal
    res = None
    attribute = 0

    try : 
        column = int(input("Input column in Data>> "))
        if column > len(field) or column < 1 :
            print ("Error : invaild column ")
            exit(0)
        
        column = column-1
        
    except ValueError : 
        print ("Error :  invaild value ...")
        exit(0)
                
    while True : 
        idx = menu()
        if idx  == 1 :
            print ("Bubble Sorting ...")
            start = timeit.default_timer()
            res = bubble_sort(data, column)
            end = timeit.default_timer()
            attribute = 1
            print ("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 2 :
            print ("Inserting Sorting ...")
            start = timeit.default_timer()
            res = insert_sort(data, column)
            end =  timeit.default_timer()
            attribute = 2
            print ("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 3 : 
            print ("Selecting Sorting ...")
            start = timeit.default_timer()
            res = select_sort(data, column)
            end =  timeit.default_timer()
            attribute = 3
            print ("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 4 :
            print ("Heap Sorting ...")
            start =  timeit.default_timer()
            res = heap_sort(data, column)
            end = timeit.default_timer()
            attribute = 4
            print ("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 5 :
            print ("Recursive Merge Sorting ...")
            data = orignal
            start =  timeit.default_timer()
            rec_merge_sort(data, column)
            end = timeit.default_timer()
            res= data
            attribute = 5
            print("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 6 :
            print ("Iteractive Merge Sorting ...")
            start = timeit.default_timer()
            res = seq_merge_sort(data, column)
            end = timeit.default_timer()
            attribute = 6
            print("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 7:
            print ("Recursive Quick Sorting ...")
            data = orignal
            start = timeit.default_timer()
            rec_quick_sort(data, column)
            end = timeit.default_timer()
            res = data
            attribute = 7
            print("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 8 :
            print ("Iteractive Quick Sorting ...")
            start = timeit.default_timer()
            res = seq_quick_sort(data, column)
            end = timeit.default_timer()
            attribute = 8
            print ("D0NE ~ !!")
            print ("execute time : %f" %(end - start))
            out_data(path, attribute, res, field, file_name)
            exit(0)

        elif idx == 0 :
            print ("bye bye ~ ")
            exit(0)
