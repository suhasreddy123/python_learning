import re
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
#<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)
