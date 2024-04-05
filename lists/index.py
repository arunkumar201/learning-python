list1 = [12, 3, 4, 5]
print(list1)

# using List constructor
list2 = list((1, 2, 3, 4))
print(list2)

list2 = list([1, 2, 3, 4, 5])
print(list2)

# with heterogeneous items
my_list3 = [1.0, 'Jessa', 3]
print(my_list3)
# Empty list
my_list4 = []
print(my_list4)

my_list4 = list()
print(my_list4)

# display the length of the list
print(len(my_list3))

# Accessing elements  from the list

# 1. we can use index to access the elements
print(my_list3[0])  # 1.0 -gives the first element the list

print(my_list3[1])  # 'Jessa' -gives the second element the list
print(my_list3[2])  # 3 -gives the third element the list
# print(my_list3[23])  # IndexError: list index out of range

# we can use index to access the element using negative indexes

print(my_list3[-1])  # 3 -gives the last element the list
print(my_list3[-2])  # 'Jessa' -gives the second last element the list
print(my_list3[-3])  # 1.0 -gives the third last element the list

# print(my_list3[-4])  # IndexError: list index out of range

# 2. we can use slicing for accessing the elements from the list  ==

print(my_list3[0:2])  # [1.0, 'Jessa'] -gives the first two elements from the list

print(my_list3[1:3])  # ['Jessa', 3] -gives the second and third elements from the list

print(my_list3[2:4])  # [3]- as we only have list of size 3

print(my_list3[42:1])  # [] - as we have list of size 3 and index 42 is out of range

my_list = [5, 8, 'Tom', 7.50, 'Emma']
# Slice the first 4 elements from the list
print(my_list[:4])
# Or
print(my_list[0:4])

# accessing the last element
print(my_list[-1])

# accessing the second last element
print(my_list[-2])

# accessing 3 values from 2
print(my_list[1:4])

# print every second element
# with a skip count 2
print(my_list[::2])

# reverse the list
print(my_list[::-1])

# getting from 2nd item to last
print(my_list[1:])
