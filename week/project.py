

number = int(input('enter number'))
def collatz(number):
    if number == 1:
            return  number
    if number % 2 == 0:
        number = number//2
    else:
        number = 3*number+1
    print(number)
    return  collatz(number)



collatz(number)
# def collatzsequence():
#    if number%2==0:
#       number==r
#      return collatz()
# else:
#    number==s
#   return collatz()**\
