import re
Phonenumregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(Phonenumregex.findall('cell:456-789-9888 mobile:789-678-7899'))

