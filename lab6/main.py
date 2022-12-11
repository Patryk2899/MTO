#!/usr/bin/env python3

import sys

def new_digit(x):
    converted_num = int(x)
    converted_num = ((converted_num*9)+1)%10
    if converted_num == 0:
        return 9
    return converted_num

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
            if check == 4:
                shouldSkip=False
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] and (format_string[idx+2] in digits) :
                if format_string[idx+3] == 'g':
                    x = int(format_string[idx+2])
                    n = len(param) - x

                    for i in param[:x]:
                        print(new_digit(i), end="")
                    check = 0
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