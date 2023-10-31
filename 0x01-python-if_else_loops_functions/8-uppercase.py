#!/usr/bin/python3

def uppercase(str):
    temp = list(str)
    for i in range(len(temp)):
        if (ord(temp[i]) > 96 and ord(temp[i]) < 123):
            temp[i] = chr(ord(temp[i]) - 32)

    print("{}".format(("").join(temp)))
