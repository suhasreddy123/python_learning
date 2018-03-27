def print_formatted(number):
    for i in range(1,n+1):
        print(i,oct(i).lstrip('0o'),hex(i).lstrip('0x'),bin(i).lstrip('0b'))
n = int(input())
print_formatted(n)
    # your code goes here
