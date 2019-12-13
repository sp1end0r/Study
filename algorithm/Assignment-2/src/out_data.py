#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

def out_data(path, name, original, result,result_rec,attribute):
    file_name = path = os.getcwd()+"/output/"+name+"_output.txt"  
    with open(file_name, "aa") as fp :
        if attribute == True :
            for string0, string1, string2 in zip(original,result, result_rec):
                string0 = "[original]"+string0+"\n"
                string1 = "[encrypted][lteractive]"+string1+"\n"
                string2 = "[encrypted][recursive]"+string2+"\n"
                fp.writelines(string0)
                fp.writelines(string1)
                fp.writelines(string2)
            print ("Successfully Creating encrpyted result data!")

        else : 
            for string0, string1, string2 in zip(original, result, result_rec):
                string0 = "[original]"+string0+"\n"
                string1 = "[decrypted][lteractive]"+string1+"\n"
                string2 = "[decrypted][recursive]"+string2+"\n"
                fp.writelines(string0)
                fp.writelines(string1)
                fp.writelines(string2)
            print ("Successfully Creating decrpyted result data!")
       
            

