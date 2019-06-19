# Assign a list to an variable named my_list
my_list = [1,2,3]

my_list1 = ['A string',23,100.232,'o']

# Grab element at index 0
print(my_list[0])
print(my_list1[1:])


# Grab everything UP TO index 3
my_list[:3]

# Reassign
my_list = my_list + ['add new item']

print(len(my_list))

#repeat the elements n times
my_list2 = my_list * 2

print(len(my_list2))

# basic method
list1 = [1,2,3]
list1.append('a')

print(len(list1))

new_list = ['a','e','x','b','c']
print(new_list.reverse())
print(new_list.sort())


lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]

first_col = [row[0] for row in matrix]
print(first_col)