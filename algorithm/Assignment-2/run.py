#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from src.cus_string import *
from src.check_crpyto import *
from src.cryptomodule import *
from src.listdir import *
from src.load_data import *
from src.out_data import *
import timeit, sys
sys.setrecursionlimit(20000)

if __name__ =="__main__":
    path = os.getcwd()
    file = list_dir(path)
    list = load_data(path, file)
    encrypt_list, decrypt_list,enc_flag, dec_flag = check_list(list)

    while True:
        if enc_flag:
            result = []
            result_rec = []
            print("Encrypted Data!")
            attribute = True

            for string in encrypt_list:
                result_string = ""
                start = timeit.default_timer()
                result.append(encrypt_string(string.rstrip("\n")))
                end = timeit.default_timer()
                print ("lteractive call execute time : %f" %(end - start))
                if len(string) > 25000 : ##문자열의 길이가 25000보다 크면 분할하여 재귀호출
                    temp = divide_string(string)
                    for i in temp :
                        result_string += encrypt_string_rec(i.rstrip("\n"))
                else :
                    start = timeit.default_timer()
                    result_string = encrypt_string_rec(string.rstrip("\n"))
                    end = timeit.default_timer()
                    print ("recursive call execute time : %f" %(end - start))

                result_rec.append(result_string)

            out_data(path, file, encrypt_list, result, result_rec, attribute)
            enc_flag = False

        elif dec_flag :
            result = []
            result_rec = []
            print("Decrypted Data!")
            attribute = False

            for string in decrypt_list:
                result_string = ""
                result.append(decrypt_string(string.rstrip("\n")))
                if len(string) > 25000 : ##문자열의 길이가 10000보다 크면 분할하여 재귀호출
                    temp = divide_string(string)
                    for i in temp :
                        result_string += decrypt_string_rec(i.rstrip("\n"))
                else : 
                    start = timeit.default_timer()
                    result_string = decrypt_string_rec(string.rstrip("\n"))
                    end = timeit.default_timer()
                    print ("execute time : %f" %(end - start))

                result_rec.append(result_string)

            out_data(path, file, decrypt_list, result, result_rec, attribute)
            dec_flag = False
        
        else : exit(0)




        

