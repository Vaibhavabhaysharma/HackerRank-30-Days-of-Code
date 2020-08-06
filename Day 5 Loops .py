#!/bin/python

import math
import os
import random
import re
import sys

i=0
result=0
n = int(raw_input())
for i in range(1,11):
    result = n*i
    print(str(n)+' x '+str(i)+' = '+str(result))
