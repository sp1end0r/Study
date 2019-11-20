#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

def out_data(path, attribute, res, field,file):
    if attribute == 0 : 
        print ("Plz Sorting data before creating out put file... ")
        exit(0)
    
    file_name = path = os.getcwd()+"/output/"+file+"_output_"+str(attribute)+".csv"
    
    with open(file_name, "w") as fp :
        string = ",".join(field)
        string += "\n"
        fp.write(string)
        for line in res:
            string = ""
            string += ",".join(line)
            string += "\n"
            fp.write(string)
                
    print ("Successfully Creating reslut data!")
    print ("============================")

