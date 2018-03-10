"""formule=(-b+-sqrt((b**2-4ac)/2a)
when equation in the form of Ax2+bx+c take co-efficients.
"""
a=float(input("enter the value of x2 multiple :"))
b=float(input("enter the value of x multiple :"))
c=float(input("enter the value constant :"))
second_part=((((b**2)-4*a*c)/2*a)**0.5)
first_root=(-b+second_part)
second_root=(-b-second_part)
print(first_root)
print(second_root)