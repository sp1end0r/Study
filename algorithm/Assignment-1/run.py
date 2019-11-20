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
            res = bubble_sort(data, column)
            attribute = 1
            print ("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 2 :
            print ("Inserting Sorting ...")
            res = insert_sort(data, column)
            attribute = 2
            print ("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 3 : 
            print ("Selecting Sorting ...")
            res = select_sort(data, column)
            attribute = 3
            print ("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 4 :
            print ("Heap Sorting ...")
            res = heap_sort(data, column)
            attribute = 4
            print ("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 5 :
            print ("Recursive Merge Sorting ...")
            rec_merge_sort(data, column)
            res= data
            attribute = 5
            print("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 6 :
            print ("Iteractive Merge Sorting ...")
            res = seq_merge_sort(data, column)
            attribute = 6
            print("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 7:
            print ("Recursive Quick Sorting ...")
            rec_quick_sort(data, column)
            res = data
            attribute = 7
            print("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 8 :
            print ("Iteractive Quick Sorting ...")
            res = seq_quick_sort(data, column)
            attribute = 8
            print ("D0NE ~ !!")
            out_data(path, attribute, res, field, file_name)

        elif idx == 0 :
            print ("bye bye ~ ")
            exit(0)