#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def divide_string(string): ##재귀 호출 처리를 위한 문자열 분할 함수
    length = len(string)//10 ##총 11개로 분할
    result = [string[i:i+length] for i in range(0, len(string), length)] ##분할된 문자열은 리스트에 저장

    return result