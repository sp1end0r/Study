#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

def out_data(path,result,result_rec,attribute):
    file_name = path = os.getcwd()+"/output/output.txt"   
    with open(file_name, "a") as fp :
        if attribute == True :
            for string1, string2 in zip(result, result_rec):
                string1 = "[encrypted][lteractive]"+string1+"\n"
                string2 = "[encrypted][recursive]"+string2+"\n"
                fp.writelines(string1)
                fp.writelines(string2)
                print ("Successfully Creating encrpyted result data!")

        else : 
            for string1, string2 in zip(result, result_rec):
                string1 = "[decrypted][lteractive]"+string1+"\n"
                string2 = "[decrypted][recursive]"+string2+"\n"
                fp.writelines(string1)
                fp.writelines(string2)
                print ("Successfully Creating decrpyted result data!")
       
            

