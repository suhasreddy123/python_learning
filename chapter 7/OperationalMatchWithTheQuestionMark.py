import re
phoneregex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1=phoneregex.search('my number is 456-567-7890')
print(mo1.group())
mo2=phoneregex.search('456-6789')
print(mo2.group())
