#!/bin/python3
import datetime

import sys
def solve(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                year = "leap"
            else:
                year = "not leap"
        else:
            year="leap"
    else:
        year="not leap"
    if year=="leap":
        print("12.09."+y)
    else:
        print(("13.09."+y))

year = int(input().strip())
y=str(year)
solve(year)
