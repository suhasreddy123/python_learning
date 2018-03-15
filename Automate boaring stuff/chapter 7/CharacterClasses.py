import re
xmasregex=re.compile(r'\d+\s\w+')#(\d+)#  will match text thaat has one or more numeric digits
#followed by a whitespace character (\s)
# followed by one or more letter/digit/underscore(\w+)
print(xmasregex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
