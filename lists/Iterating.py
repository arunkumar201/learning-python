list1 = [1, 2, 3, 4, 56, 7]

# for i in list1:
#     print(i)

for i in range(0, len(list1)):
    print(i, "->", list1[i], end=" ,")

# Operations on List
# 1. Append(element)-it allows us to add one element at the end of the list

list1.append(123)
print(list1)
# below code will add the list in the list (nested list)
list1.append([12, 3, 4, 5, 3, 5, 3, 5, 3, 5, 34, 4, 3, 4])
# 2. Extend(list)-it allows us to add multiple elements at the end of the list
list1.extend([1, 2, 3, 4])
print(list1)

print(list1.count(123))

# insert an element at specified position in the list
# insert(index, object)

res = list1.insert(1, 21)
print(list1)

# insert nested list at  position 3
list1.insert(3, [25, 50, 75])
print(list1)

# Modify the individual item.
list1[0] = ["hello", "world"]
print(list1)

# modify the multiple items
list1[0:2] = ["hello", "world"]
print(list1)  # it will modify the list from index 0 to index 2 and replace the items with hello and world

# Modify all items
for i in range(0, len(list1)):
    list1[i] = 0
print(list1)

# Removing elements from a List
# 1. remove()- takes the item values and remove the first occurrence of it
list1.remove(0)
print(list1)

# remove the item by index ,
# pop(index)- removes the item at the specified index and returns the removed item
res = list1.pop(2)
print(res, "removed item")
print(list1)

# clear()- it will remove the all items from the list
# list1.clear()
# print(list1)


# Remove all occurrence of a specific item
print(list1, "before removing all occurrence of 0")
for i in list1:
    list1.remove(0)

print(list1, "after removing all occurrence of 0")

# Remove the range of items
del list1[0:3]  # it will delete the items from index 0 to index 2
print(list1)

# Finding an element in the list - it will take an item and returns the index of that item (first occurrence)
# if not found then it will return valueError
# res = list1.index(30)
# print(res)

# Concatenation of two lists
list_A = [1, 2, 3, 4]
list_B = [1, 2, 3]
print(list_B + list_A)
print(list_A)
print(list_B)
# //also we can use the extend()
list_B.extend(list_A)
print(list_A)
print(list_B)

# Copy the list
new_list = ["a", "b", "c", "d", "e", "f", "g"]
new_list1 = new_list
print(new_list1)
print(new_list1 is new_list)

# also we can use copy() function
new_list2 = new_list.copy()
print(new_list2)

# List operations
# 1.sort()- it will sort the list-default sort is ascending
list1.sort()

# reverse()
new_list.reverse()
print(new_list)

# max() and min() - it will return the maximum and minimum value from the list
print(max(list_A))
print(min(list_A))
print(sum(list_A))
# if we want to delete the list we can use del keyword
del list1
