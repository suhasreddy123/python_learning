n_of_stocks=int(input())
item_list= set(list(map(int, input().strip().split(' '))))
n_of_stocks=int(input())
item_list1= set(list(map(int, input().strip().split(' '))))
a=[]
a=item_list-item_list1
print(len(a))
