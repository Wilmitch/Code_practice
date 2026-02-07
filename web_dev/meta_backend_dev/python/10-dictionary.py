#!/usr/bin/python3
dict1 = {1: 'Coffee', 2: 'Tea', 3: 'Juice', 'Name': 'William'}
print(dict1)
print(dict1[1])

dict1[2] = 'Mint Tea'
print(dict1[2])

for key, value in dict1.items():
    print("{} : {}".format(key, value))