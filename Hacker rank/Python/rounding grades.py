#!/bin/python3

import sys


def solve(grades):
    grade_n = []
    for marks in grades:
        if marks >= 38:
            if marks % 5 == 3:
                x=marks+2
                grade_n.append(x)
            elif marks % 5 == 4:
                y = marks + 1
                grade_n.append(y)
            else:
                grade_n.append(marks)
        else:
            grade_n.append(marks)
    print("\n".join(map(str, grade_n)))


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
solve(grades)





