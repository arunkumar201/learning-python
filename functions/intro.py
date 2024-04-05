import random

food = ["pizza", "burger", "noodles", "pasta", "ice cream"]
randomFood = random.choice(food)
print(f"I love {randomFood}")
randomAge = random.randint(1, 20)
print("My age is", randomAge)
if 18 <= randomAge <= 40:
    print("I am an adult")
elif 15 <= randomAge < 18:
    print("I am a teenager")
elif 6 <= randomAge <= 14:
    print("I am just a kid")
elif randomAge > 40:
    print("I am old")
else:
    print("I are baby")


# famous example that uses random package


def generate_password():
    password_length = random.randint(8, 20)  # random password length between 8 and 20 characters
    pass_word = ''
    for i in range(password_length):
        # Generating a random ASCII value for uppercase letters (65-90),
        # lowercase letters (97-122), or special characters (33-47)
        pass_word += chr(random.choice([random.randint(65, 90), random.randint(97, 122), random.randint(33, 47)]))
    return pass_word


'''
generates a random password of length between 8 and 20 characters
and consists up of uppercase letters, lowercase letters, and special characters 
'''

password = generate_password()
print(password)
