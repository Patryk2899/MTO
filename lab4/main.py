#!/usr/bin/env python3

import sys

def reverse_number(n):
    rev = 0
    
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'g':
                param = int(param)
                param = reverse_number(param)
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())