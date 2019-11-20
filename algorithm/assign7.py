#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#file name : assign7.py
#

def search_name(list1, list2, num): #list 1 : 학생이름이 담긴 리스트, list2 : 학생번호가 있는 리스트, num : 학생번호
    length = len(list2)
    res = ""
    for i in range(0,length):
        if num == list2[i]: 
            res = list1[i]
            break
        else : 
            res = "?"
    return res


if __name__ == "__main__":
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]

    print (stu_no)
    print (stu_name)

    try : 
        num = int(input("input number for searching student's name >> "))
        print ("result : %s" % search_name(stu_name,stu_no, num) )
    except  ValueError :
        print ("ValueError : wrong number ..")
