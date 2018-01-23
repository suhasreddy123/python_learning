import pprint
string='hello world'
count={}
for character in string:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)