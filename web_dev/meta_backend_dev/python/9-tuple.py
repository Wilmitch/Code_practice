#!/usr/bin/python3
my_tuple = (1, "string", 4.5, True)
print(my_tuple)

print(my_tuple.count("string"))

print(my_tuple.index(4.5))

for item in my_tuple:
    print("Value: ", item)
    