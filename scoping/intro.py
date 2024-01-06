from datetime import datetime


def isOdd(x: int) -> None:
    y = 12
    if x % 2 == 0:
        print("It is not an odd number", "value of global variable a is :", a)
        return

    print("Number is odd")


# isOdd(56)
a = 100
print(type(isOdd))
isOdd(a)

# print(y) #gettin y is not defined

global_x = 100


def getCurrentTime():
    global global_x  # Declare global_x before using it
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current local time:", current_time)
    print("Global variable value is", global_x)
    global_x = 233
    print(global_x)
    del global_x
    x = 33
    print(type(id(x)))


getCurrentTime()
