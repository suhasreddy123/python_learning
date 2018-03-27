#Python Program to Find ASCII Value of Character
char_list=[]
for char in range(5):
   char_list.append(input())
for char in char_list:
    print(char,ord(char))
c=ord("b")-ord("B")
print(c)
