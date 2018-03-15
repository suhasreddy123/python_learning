#check a number is palindrome
"""num=int(input())
if num ==(str((num)[::-1])):
    print("number is palindrome")
else:
    print("number is not pallindrome")"""
"""num=input()
val = int(num)
if num == str(num)[::-1]:
    print('The given number is PALINDROME')
else:
    print('The given number is NOT a palindrome')"""
string=input("enter a string:")
str=string.swapcase()
str2=str[::-1]
print(str2)
"""new_string=""
for char in string:
    if char.islower():
        new_string+=char.upper()
    else:
        new_string+=char.lower()
#print(new_string)
print(new_string[::-1])"""