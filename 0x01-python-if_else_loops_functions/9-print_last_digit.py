#!/usr/bin/python3
def print_last_digit(num):
    num = abs(num) % 10
    print(num, end="")
    return num
