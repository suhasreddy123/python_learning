import re
batregex=re.compile(r'Bat(wo)+man')
mo=batregex.search('the adventure of Batwowowoman')
print(mo.group())
