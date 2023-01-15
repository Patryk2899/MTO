#!/usr/bin/env python3

import sys

def change_characters(param):
    hex_to_str = str(param)
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
        else:
            temp = hex_to_str[i]
        result = result + temp
    return result

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                hex_format = hex(int(param))
                print(change_characters(hex_format),end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
