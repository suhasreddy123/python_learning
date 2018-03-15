import re
heroregex = re.compile (r'Batman| Tina Fey')
#mo = heroregex.search('Batman and Tina Fey.')
#print(mo.group())
# it only searches for the first one
mo2=heroregex.search('Tina Fey and Batman.')
print(mo2.group())
