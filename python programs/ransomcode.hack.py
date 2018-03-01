def ransom_note(magazine, ransom):
    length_mag = len(magazine)
    length_ran = len(ransom)
    #print("this is",ransom)
    compare=[]
    for w in magazine:
        if w in ransom:
            compare.append(w)
    if (length_mag==num_mag_words)and (length_ran==num_ransom_words):
        if (ransom == compare):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

num_mag_words,num_ransom_words = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')

answer = ransom_note(magazine, ransom)
