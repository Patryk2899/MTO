#!/usr/bin/env python3

import sys

def change_characters(param):
    hex_to_str = str(param)
    count = 0
    for i in hex_to_str:
        if i == 'a':
            hex_to_str[count] = 'g'
        if i == 'b':
            hex_to_str[count] = 'h'
        if i == 'c':
            hex_to_str[count] = 'i'
        if i == 'd':
            hex_to_str[count] = 'j'
        if i == 'e':
            hex_to_str[count] = 'k' 
        if i == 'f':
            hex_to_str[count] = 'l'
        count = count + 1       
    return hex_to_str

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                hex_format = hex(int(param))
                print(hex_format,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
