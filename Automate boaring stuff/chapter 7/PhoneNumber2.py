import re

phonenumregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumregex.search('My number is 423-555-4242.')
print('phone number found:' + mo.group())