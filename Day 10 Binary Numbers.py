import math
import os
import random
import re
import sys
def decimalToBinary(n):
    if not n:
        return 0
    num= bin(n).replace("0b", "")
    return len(max(num.replace('0', ' ').split(), key=len))


if __name__ == '__main__': 
    n = int(input())
    max_ones=decimalToBinary(n)
    num=0
    print(max_ones)
