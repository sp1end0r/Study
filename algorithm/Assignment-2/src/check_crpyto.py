#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def check_list(list): ## 파일에서 입력받은 내용을 암호화할 문자열과 복호화할 문자열이 담긴 리스
    encrpyt_list = []
    decrpyt_list = []
    enc_flag = False
    dec_flag = False
    for data in list:
        if data[0] == "#":
            encrpyt_list.append(data[1:])
            enc_flag = True
        
        elif data[0] == "@":
            decrpyt_list.append(data[1:])
            dec_flag = True

        else :
            print ("invaild data..")
            exit(0)

    return encrpyt_list, decrpyt_list, enc_flag, dec_flag