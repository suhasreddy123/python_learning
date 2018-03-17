import textwrap
from collections import OrderedDict
string="AABCAAADA"
k=3
def merge_the_tools(string, k):
    # your code goes here
    a=(textwrap.wrap(string,k))
    for item in a:
        print("".join(OrderedDict.fromkeys(item)))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)