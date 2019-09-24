#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def find_max(data):
    length = len(data)
    max_data = data[0]
    try : 
        for i in range (1, length):
            if data[i] > max_data:
                max_data = data[i]
        return max_data

    except UnboundLocalError:
        print ("FindMaxData : UnboundLocalError : A few data ..")
        exit(0)

def find_min(data):
    length = len(data)
    min_data = data[0]
    try :
        for i in range(1, length):
            if data[i] < min_data:
                min_data = data[i]
        return min_data

    except UnboundLocalError:
        print ("FindMinData : UnboundLocalError : A few data ..")
        exit(0)

def input_interface():
    try : 
        data = list(map(float, input("input your number >>").split(" ")))
        return data

    except ValueError:
        print("ValueError : pleses input number ...")
        return

def menu(data):
    print ("============================")
    print ("         Select contents")
    print ("============================")
    print ("1. Input data in List")
    print ("2. Find Maximum data in List")
    print ("3. Find Minimum data in List")
    print ("0. Exit ")
    print ("============================")
    if not data : 
        print ("List is empty!")
    else : 
        print (data)
    print ("============================")
    try : 
        res = int(input(">> "))
        return res
    
    except ValueError : 
        print ("Error invaild value..")
        return 

if __name__ == "__main__":
    
    data = []
    while True :

        index = menu(data)
        if index == 0 :
            print ("bye bye ~ ")
            exit(0)

        elif index == 1 :
            data = input_interface()

        elif index == 2 :
            max_data = find_max(data)
            print ("Max data in List : %.2f" % max_data)

        elif index == 3 :
            min_data = find_min(data)
            print ("Minimun data in List : %.2f" % min_data)

        else : 
            print ("Error : invaild menu number ..")
