import string 
import random 
_LENGTH = 20000
choice = int(input("choice (0 = encrypt, 1 = decrpyt) : "))
if choice == 0 :
    string_pool = string.ascii_letters
    result = "" 
    for i in range(_LENGTH) : 
        result += random.choice(string_pool) 
    result= "#"+result+"\n"
    with open("input3.txt", "a") as fp:
        fp.writelines(result)

else :
    string_pool = string.ascii_letters
    result = "" 
    for i in range(_LENGTH) : 
        result += random.choice(string_pool)+str(random.randint(1,9))
    result= "@"+result+"\n"
    with open("input3.txt", "a") as fp:
        fp.writelines(result)

