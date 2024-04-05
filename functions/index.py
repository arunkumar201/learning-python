def getEvenValues(nums):
    even = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
    return even


even_list = getEvenValues([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 112,
                           3, 4, 5, 6, 7, 8, 9, 10, 101, 102, 103, 104, 105])
print(even_list)

# Dictionary in  python

dict1 = {"name": "Arun", "age": 24, "city": "Bangalore"}
# get the type
print(type(dict1))
print(dict1)
print(dict1["name"])
print(dict1.get("age"))

print("items are:-", dict1.items())
print("Keys are:-", dict1.keys())
print("Values are :-", dict1.values())
dict2 = dict(name="Arun", age=24, city="Bangalore")
print(dict2)
# Create a copy of the dictionary
dict3 = dict1.copy()
print(dict3)
print(type(len(dict3.values())))
