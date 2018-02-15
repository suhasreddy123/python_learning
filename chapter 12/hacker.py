fl=open("/home/ramesh/Downloads/Untitled Document")
content=fl.read()
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
#for word in content.split():
word_count=len(content.split())
n=word_count
count=0
word=content.split()
for i in range(0,n,1):
    if content.split()[i]==content.split()[i+1]:
        count=count+1
        print(count)
