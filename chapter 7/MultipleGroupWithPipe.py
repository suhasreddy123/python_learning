import re
batregex = re.compile(r'Bat(man|mobile|copter|baat)')
mo = batregex.search('Batmobile copter wheel')
print(mo.group())# it reeturns the full mathed text
print(mo.group(1))# it returns the only part of the mathed text






