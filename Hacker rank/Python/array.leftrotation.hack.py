def array_left_rotation(elements, number_of_elements,number_of_rotations):
    temp = elements[:number_of_rotations]
    del elements[:number_of_rotations]
    elements = elements.extend(temp)
temp=[]
number_of_elements,number_of_rotations = map(int, input().strip().split(' '))
elements = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(elements,number_of_elements,number_of_rotations);
elements_join=" ".join(str(item) for item in elements)
elements_split=" ".join(elements_join.split())
print(elements_split)