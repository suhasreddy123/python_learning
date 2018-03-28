def capitalize(string):
    sentence=string.split(' ')
    list1=[]
    for i in sentence:
        list1.append((i.capitalize()))
    return (" ".join(list1))
string = input()
capitalized_string = capitalize(string)
print(capitalized_string)