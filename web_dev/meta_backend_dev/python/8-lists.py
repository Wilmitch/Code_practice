#!/usr/bin/python3
list1 = [1,2,3,4,5]
print(*list1)

list1.insert(len(list1), 6)
print(list1)

list1.append(7)
print(list1)

list1.extend([8,9])
print(list1)

list1.pop(4)
print(list1)

del list1[2]
print(list1)

for num in list1:
    print("Value: ", num)