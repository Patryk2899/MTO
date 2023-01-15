#!/usr/bin/env python3

import sys

def change_characters(param, count):
    hex_to_str = str(param)
    hex_to_str = hex_to_str[2:]
    
    if len(hex_to_str) < count:
        count = count -len(hex_to_str)
        for i in range(1, count):
            "0" + hex_to_str

    result = ""
    for i in range(0, len(hex_to_str)):
        if hex_to_str[i] == 'a':
            temp = 'g'
        elif hex_to_str[i] == 'b':
            temp = 'h'
        elif hex_to_str[i] == 'c':
            temp = 'i'
        elif hex_to_str[i] == 'd':
            temp = 'j'
        elif hex_to_str[i] == 'e':
            temp = 'k' 
        elif hex_to_str[i] == 'f':
            temp = 'l'
        elif hex_to_str[i] == '0':
            temp = 'o'
        else:
            temp = hex_to_str[i]
        result = result + temp
    return result

def my_printf(format_string,param):
    numbers = "0123456789"
    shouldDo=True
    count = 4
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+2] in numbers and format_string[idx+3] == "j" :
                count = int(format_string[idx+2])
                hex_format = hex(int(param))
                print(change_characters(hex_format, count),end="")
                count = 0
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if count == 4: 
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
