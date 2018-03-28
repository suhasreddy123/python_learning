n_items,i_not = input().strip().split(' ')
n_items,i_not = [int(n_items), int(i_not)]
item_list= list(map(int, input().strip().split(' ')))
value_charged=int(input())
value_charged=int(value_charged)
new_list=item_list
new_list.pop(i_not)
value_actual=((sum(new_list))/2)
if (value_charged==value_actual):
    print("Bon Appetit")
else:
    print(value_charged-value_actual)