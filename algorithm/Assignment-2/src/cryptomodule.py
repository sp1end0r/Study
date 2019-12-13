#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def encrypt_string(string):
    stack = []                              #중복 문자열 처리를 위한 저장공간 사용
    length = len(string)    
    res = ""
        
    for cur in range(0,length-1):
        stack.append(string[cur])           #현재 위치에 있는 문자를 stack에 저장

        if cur + 1 == length -1 :           #다음 위치가 문자열의 끝이면
            if stack[0] != string[cur+1]:   #스택에 들어있는 문자과 문자열의 마지막 문자가 다르다면
                stack_length = len(stack)   #현재 스택에 담겨진 문자 개수 세기
                res += stack[0]+str(stack_length)+string[cur+1]+"1" #결과 문자열 만들기
            else :
                stack.append(string[cur+1]) #스택에 들어있는 문자와 문자열의 마지막 문자가 같다면 스택에 문자열의 마지막 문자 저장
                stack_length = len(stack)   #현재 스택에 담겨진 문자 개수 세기
                res += stack[0]+str(stack_length) # 결과 문자열 만들기
                stack = []                        # 스택초기화
        
        elif stack[0] != string[cur+1]:     # 스택에 저장된 문자가 문자열의 다음 문자와 다르다면
            stack_length = len(stack)       # 현재 스택에 담겨진 문자 개수 세기
            res += stack[0]+str(stack_length) # 결과 문자열 만들기
            stack=[]

    return res

def decrypt_string(string):
    stack = []                              #중복 문자열 처리를 위한 저장공간 사용
    length = len(string)
    res = ""

    for cur in range(0, length):
        stack.append(string[cur])           #스택에 현재 위치의 데이터 저장
       
        if (stack[-1].isdigit()):           #스택의 top이 숫자라면
            str_length = int(stack[-1])     #중복된 문자의 길이는 스택의 top 값
            del stack[-1]                   #스택의 top값 pop
            for _ in range(0, str_length):  #중복된 문자열의 길이만큼 스택의  top 값을 이용하여 문자열 복원
                res += stack[-1]
    return res

def encrypt_string_rec(string):
    if not string:                          #재귀 종료 조건
        return ""
    else:   
        characteracter = string[0]               #문자열의 첫글자부터 시작
        length = len(string)
        i = 1   
        while i < length and characteracter == string[i]: #characteracter가 문자열에서 중복된것이 발생할때까지
            i += 1                                      #중복된 문자 카운팅
        return characteracter + str(i) + encrypt_string_rec(string[i:]) # 결과 문자열를 만들면서 재귀 호출


def decrypt_string_rec(string):
    if not string:                           #재귀 종료 조건
        return ""
    else:
        character = string[0]                     #문자열의 첫글자는 반복하고자하는 문자
        length = string[1]                 #문자열의 두번째 글자는 반복횟수
        return character * int(length) + decrypt_string_rec(string[2:]) #결과 문자열을 만들면서 재귀호출
    
       
    


