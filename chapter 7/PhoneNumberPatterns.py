import re
phoneNumregex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumregex.search('my phone number is (465) 666-7777.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups)
