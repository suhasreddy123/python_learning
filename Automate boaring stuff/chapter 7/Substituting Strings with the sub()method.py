import re
namesregex= re.compile(r'agent \w+')
print(namesregex.sub('CENSORED','Agent alice gave the secret document to agent bob'))
