print("Hello World")

for i in range(10):
    print("Hello World")

i = 12
my_sum = 9


def summation(x):
    return x * 10

for i in range(100):
    my_sum += i
    i = i / summation(my_sum)

print(my_sum)
