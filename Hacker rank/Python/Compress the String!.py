"""a=input()
print(a)
b=set(a)
print(b)
#1222311
import collections
a = [1,2,2,2,3,1,1]
counter=collections.Counter(a)
print(counter)
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common()"""
def countFreq(A):
   n=len(A)
   count=[0]*n                     # Create a new list initialized with '0'
   for i in range(n):
      count[A[i]]+= 1              # increase occurrence for value A[i]
   return [x for x in count if x]
x=[1,2,2,2,3,1,1]
print(countFreq(x))



