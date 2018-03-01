fl=open("/home/ramesh/Downloads/Untitled Document")
content=fl.read()
print(content)
longest = 0
for word in content.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word
print("char count# ", len(content))
print(content.split(" "))
print ("word count# ", len(content.split()))
print ("line count# ", len(content.split("\n")))
print("The longest word is",longest_word,"and the length of word is",longest)
#Wprd reverse in the string
n=len(content.split())
print(n)
for i in range (0,n):
    a=content.split()[i][::-1]
    print(a,end=" ")
#frequency of word
#stg=content.split()
#dict={}
#def word_frequency(stg):
    #for i in range (0,n):
        #if stg[i]==stg[i+1]:

#x=input(content)
#y=x.split()
#y.sort()
#for y in sorted(y):
    #print (y)



from collections import Counter

mysentence = content

mysentence = dict(Counter(mysentence.split()))
for i in sorted(mysentence.keys()):
    print ('"'+i+'" is repeated '+str(mysentence[i])+' time.')