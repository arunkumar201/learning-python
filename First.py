print("Hello World")

for i in range(10):
    print("Hello World")

i = 12
my_sum = 9


def summation(x):
    return x * 2


print(3 // 3)

for i in range(10):
    my_sum += i
    i = i / summation(my_sum)

print(my_sum)

value = 5
print(type(value))
print(type(value) == int)
value = str(value)
print(isinstance(value, str))
value = float(value)
print(isinstance(value, float))
