#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    n = 0
    x = 0
    check = 0
    #print(format_string)
    shouldDo=True
    shouldSkip=False
    for idx in range(0,len(format_string)):
        if shouldSkip:
            check = check + 1
            if check == 3:
                shouldSkip=False
        if shouldDo:
            if format_string[idx] == '#' and (format_string[idx+1] in digits) :
                if format_string[idx+2] == 'g':
                    x = int(format_string[idx+1])
                    n = len(param) - x
                    print('9'*n, end="")
                    print(param[:x],end="")
                    shouldSkip=True
                    shouldDo=False
            else:
                if not shouldSkip:
                    print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())