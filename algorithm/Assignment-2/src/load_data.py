#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

def load_data(path):
    file_name = path+"/input/report_input_usr-dict-words.en-src.txt"
    with open(file_name, "r") as fp :
        temp = fp.readlines()
    
    print ("============================")
    print ("Loading Data... DONE :)")

    return temp

