#!/bin/python3

import sys
from datetime import *

def timeConversion(m2):
    in_time = datetime.strptime(m2, "%I:%M:%p")
    result= datetime.strftime(in_time, "%H:%M")

s = input().strip()
result = timeConversion(s)
print(result)