def separateNumbers(s):
    num_stg=list(map(int,s))
    i=0;
    value = sum(num_stg)
    answer=value%10
    if num_stg[i]<num_stg[i+1]:
        print("T",answer)
    else:
        print("F")
q = int(input().strip())
sm=[]
for a in range(q):
    s = input().strip()
    separateNumbers(s)