import re
nameregex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo= nameregex.search('First Name: A2 Last Name:Sweigart')
print(mo.group(1))
print(mo.group(2))
