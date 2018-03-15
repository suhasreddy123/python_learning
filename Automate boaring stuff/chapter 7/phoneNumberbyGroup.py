import re
phonenumregex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumregex.search('my number is 432-456-6767.')
print(mo.group(0))

print(mo.group(1))

print(mo.group(2))
print(mo.groups())


