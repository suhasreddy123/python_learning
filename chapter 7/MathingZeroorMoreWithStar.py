import re
batregex=re.compile(r'Bat(wo)*man')
mo=batregex.search('The adventures of Batman')
print(mo.group())
mo=batregex.search('The adventures of Batwoman')
print(mo.group())
mo=batregex.search('The adventures of Batwowowowoman')
print(mo.group())
#For 'Batman', the (wo)* part of the regex matches zero instances of wo in the string;
#  for 'Batwoman', the (wo)* matches one instance of wo; and
# for 'Batwowowowoman', (wo)* matches four instances of wo.