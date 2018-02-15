fl=open("C:\\Users\\ramesh-home\\Desktop\\New Text Document.txt")
content=fl.read()

print("char count# ", len(content))

print(content.split(" "))
print ("word count# ", len(content.split(" ")))
print ("line count# ", len(content.split("\n")))

