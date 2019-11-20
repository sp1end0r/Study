#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os 

def list_dir(path):
    path = path + "/input"
    file_list = os.listdir(path)
    print ("file list : {}".format(file_list))
    
    file_name = str(input("Input file name : "))
    if not os.path.isfile(path+"/"+file_name) : 
        print ("Not existed File ..")
        exit (0)
        
    return file_name