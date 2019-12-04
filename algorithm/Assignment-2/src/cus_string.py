#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def divide_string(string):
    length = len(string)//10
    result = [string[i:i+length] for i in range(0, len(string), length)]

    return result