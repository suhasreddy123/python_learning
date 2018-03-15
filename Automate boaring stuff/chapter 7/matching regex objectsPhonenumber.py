import re
phn='423-567-7989'

#phn='345-555-5656'
if re.search(r"\d{3}-\d{3}-\d{4}",phn):
    print("it is phone number")
else:
    print("it is not a phone number")
