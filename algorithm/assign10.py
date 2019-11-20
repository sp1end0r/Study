#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 회문 탐색

def palindrome(data):
    length = len(data)

    mid = length//2
    start = 0
    end = length-1
    for i in range(0,mid):
        if data[start+i] != data[end-i]:
            return False
        
    return True

print (palindrome("1oW"))
print (palindrome("WoW"))


print (palindrome("W00o00W"))
print (palindrome("W12o00W"))    
