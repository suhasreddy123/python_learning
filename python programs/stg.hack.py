def string_oddeven(inputs):
    for input in inputs:
        even_chars = []
        odd_chars = []
        for i in range(0, len(input)):
            if i % 2 == 0:
                even_chars.append(input[i])
            else:
                odd_chars.append(input[i])
        print("".join(even_chars) + " " + "".join(odd_chars))
t = int(input())
inputs = []
for i in range(t):
    inputs.append(input())
string_oddeven(inputs)











