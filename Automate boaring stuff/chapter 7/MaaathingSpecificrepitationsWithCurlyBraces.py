import re
haregex=re.compile(r'(ha){3,5}')
mo=haregex.search('hahahahahaha')
print(mo.group())

