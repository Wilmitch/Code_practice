#!/usr/bin/python3
#Assigning variables with values
a = b = c = 10
print(a)
print(b)
print(c)

#Using commas to assign values
a,b,c = 1,2,3
print(a)
print(b)
print(c)

#Deleting variables
del a

print(a) #NameError: name 'a' is not defined
print(b)
print(c)
