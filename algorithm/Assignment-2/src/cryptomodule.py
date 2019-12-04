#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def encrypt_string(string):
    stack = []
    length = len(string)
    res = ''
        
    for cur in range(0,length-1):
        stack.append(string[cur])

        if cur + 1 == length -1 :
            if stack[0] != string[cur+1]:
                stack_length = len(stack)
                res += stack[0]+str(stack_length)+string[cur+1]+"1"
            else :
                stack.append(string[cur+1])
                stack_length = len(stack)
                res += stack[0]+str(stack_length)
                stack = [] 
        
        elif stack[0] != string[cur+1]:
            stack_length = len(stack)
            res += stack[0]+str(stack_length)
            stack=[]

    return res

def decrypt_string(string):
    stack = []
    length = len(string)
    res = ''

    for cur in range(0, length):
        stack.append(string[cur])
       
        if (stack[-1].isdigit()):
            str_length = int(stack[-1])
            del stack[-1]
            for i in range(0, str_length):
                res += stack[-1]
    return res

def encrypt_string_rec(string):
    if not string:
        return ""
    else:
        last_char = string[0]
        max_index = len(string)
        i = 1
        while i < max_index and last_char == string[i]:
            i += 1
        return last_char + str(i) + encrypt_string_rec(string[i:])


def decrypt_string_rec(string):
    if not string:
        return ""
    else:
        char = string[0]
        quantity = string[1]
        return char * int(quantity) + decrypt_string_rec(string[2:])
    
       
    


