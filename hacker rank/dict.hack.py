n=int(input())
phone_book={}
for i in range(0,n):
    entry=str(input()).split(" ")
    name=entry[0]
    phone=int(entry[1])
    phone_book[name]=phone
print(phone_book)
for j in range(0,n):
    name=str(input())
    if name in phone_book:
        phone=phone_book[name]
        print(name+" = "+str(phone))
    else:
        print("not found")
