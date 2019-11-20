#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def menu():
    print ("============================")
    print ("         Select contents")
    print ("============================")
    print ("1. Bubble Sorting")
    print ("2. Insertion Sorting")
    print ("3. Selection Sorting")
    print ("4. Heap Sorting")
    print ("5. Recursive Merge Sorting")
    print ("6. Iteractive Merge Sorting")
    print ("7. Recursive Quick Sorting")
    print ("8. Iteractive Quck Sorting")
    print ("0. Exit ")
    print ("============================")

    try : 
        res = int(input(">> "))
        if res < 0 or res > 8 :
            print ("Error : invaild value ...")
            exit(0)
        return res
    
    except ValueError : 
        print ("Error :  invaild value ...")
        exit(0)