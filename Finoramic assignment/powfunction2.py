"""def exponent(x, n):
    if (n <0):
        return exponent(1 / x, -n);
    elif( n == 0 ):
        return  1;
    elif (n == 1):
        return  x ;
    elif( n%2==0):
        return exponent(x * x,  n / 2);
    else:
        return x * exponent(x * x, (n - 1) / 2);
print(exponent(2,3)%3)"""
###############################################################################
"""def pow(x,n,d):
    return ((x**n)%d)
print(pow(2,3,3))"""
###################################################################
"""def calp(x,y,z):
    t = 1;
    for j in range (0,y,1):
        t = (t*(x%z))%z;
    return t;
print(calp(2,3,3))
#Hint : (ab) mod n = ((a mod n) (b mod n)) mod n"""
########################################################
def compute(x,y,z):
    r = x % z
    for i in range(y-1):
        r = r * x
        r = r % z
    return r;
print(compute(2,3,3))
###########################################################