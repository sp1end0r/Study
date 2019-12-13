#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

def load_data(path, name):
    file_name = path+"/input/"+name
    with open(file_name, "r") as fp :
        temp = fp.readlines()
    
    print ("============================")
    print ("Loading Data... DONE :)")

    return temp

