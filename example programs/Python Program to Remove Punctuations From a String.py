#Python Program to Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string="suhas:&^%$%dhjgndhrjvdfhs()&&^%dfgh"
no_punct=" "
for char in string:
    if char not in punctuations:
        no_punct+=char
print(no_punct)