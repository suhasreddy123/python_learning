#Python Program to Shuffle Deck of Cards
import itertools,random
deck=list(itertools.product(range(1,14),["spades","heart","daimonds","club"]))
random.shuffle(deck)
print("yougot:")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])