a = input()
b = input()
count = [0] * 26
offset = ord('a')
for char in a:
	count[ord(char) - offset] += 1
for char in b:
	count[ord(char) - offset] -= 1
total = 0
for value in count:
	total += abs(value)
print(total)

