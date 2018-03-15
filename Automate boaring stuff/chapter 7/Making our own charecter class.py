import re
vowelregex = re.compile(r'[aeiouAeIOU]')
print(vowelregex.findall('Robocop eats baby food. BABY FOOD.'))
