n = int(input())
student_marks = {}
new_list=[]
sum_list=[]
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    new_list=student_marks[query_name]
l=len(new_list)
sum_list=sum(new_list)
average=sum_list/l
print("%.2f" % average)

