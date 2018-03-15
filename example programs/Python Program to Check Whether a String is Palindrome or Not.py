#Python Program to Check Whether a String is Palindrome or Not
#abc=cba
stg=input()
reverse=stg[::-1]
if stg==reverse:
    print("palindrome")
else:
    print("Not palindrome")
