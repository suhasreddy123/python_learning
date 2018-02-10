lower=1
upper=1000
count=0
for num in range (lower , upper+1):
    if num>1:
        for i in  range (2,num):
            if (num%i==0):
                #print(num,'num is not prime')
                break
        else:
            print(num)