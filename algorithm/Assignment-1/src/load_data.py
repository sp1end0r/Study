#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

def load_data(path, file):
    file_name = path+"/input/"+file
    with open(file_name, "r") as fp :
        temp = list()
        while True:
            line = fp.readline()
            line = line[:-1]
            if not line : break
            temp.append(line.split(','))
    
    field = temp[0]
    del temp[0]
    print ("============================")
    print ("Loading Data... DONE :)")
    print ("Field in Data : {}".format(field))
    print ("Example in Data : {}".format(temp[0]))

    return temp, field

