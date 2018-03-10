#Python Program to Check Leap Year
"""The year can be evenly divided by 4;
If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400. Then it is a leap year."""

year=int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("year is leap")
        else:
            print("not leap year")
    else:
        print("is leap year")
else:
    print("not leap year")
