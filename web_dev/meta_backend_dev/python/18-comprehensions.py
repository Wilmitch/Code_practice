#!/usr/bin/python3
data = [2,3,5,7,11,13,17,19,23,29,31]
# List comprehensions
data = [x+3 for x in data]
print(data)
data1 = [x for x in data if x%4 == 0]
print(data1)

nines = [x for x in range(100) if x%9 == 0]
print(nines)

# Dictionary comprehension
dict1 = {x:x*2 for x in range(12)}
print(dict1)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

num_dict = {x:x**2 for x in number}
print(num_dict)

months_dict = {key:value for (key, value) in zip(number, months)}
print(months_dict)

# Set comprehensions
data2 = {x for x in range(12)}
print(data2)

# Generator comprehension
data3 = (x for x in range(12))
print(data3)
for item in data3:
    print(item)