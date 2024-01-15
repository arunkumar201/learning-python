# first way to create a tuple using () brackets

t1 = (1, 2, 3, 4, 5, "error", "success", "success", "hello world ")
print(t1)
# //display the length of the t1
print(len(t1))
print(type(t1))
print(t1[1:3])
print((t1[-5:-1]))

# second way to create a tuple using Tuple constructor

t2 = tuple(())

print(t2)

# Packing and Unpacking
packaging = 1, 2, 3, 4, 5, 5
print(packaging)
print(type(packaging))
print(len(packaging))

# un-packaging
# In case we assign fewer variables than the number of
# items in the tuple, we will get the value error with the message too many values to unpack
i, j, k, l, m, n = packaging
print(i)

# //iterating over tuple

print("iterating over tuple")
for i in packaging:
    # print(i, end=' ')
    print(i, sep='\n')

for i in range(-6, 0):
    print(packaging[i], end=", ")

# nested tuples
print('\n')
nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")
print(nested_tuple[1])

print(12 + 23)

print(1 - 1 + 23 / 3)

for i in range(10):
    print(i, end="")
    print(type(i))

# iterate a nested tuple
# for i in nested_tuple:
#     print("tuple", i, "elements")
#     for j in i:
#         print(j, end=", ")
#     print("\n")

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(max(num))

foo = (True, True, True, False)

print(all(foo))

print(any(foo))
foo1 = ()
print(any(foo1))

t1 = (10, 20, 30, 40, 10, "10")
t2 = (60, 70, 80, 60, 4)

# print(t1 * 500)


print(t1[0:4:2])
print(t1.count(10))
print("index example")
print(t1.index(40))
