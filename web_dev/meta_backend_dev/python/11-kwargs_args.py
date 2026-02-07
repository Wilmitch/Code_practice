#!/usr/bin/python3
#ARGS
def sum_of(*args):
    sum = 0
    for num in args:
        sum += num
    return round(sum, 2)

print(sum_of(2,4,5,6,5))

#KWARGS
def add_of(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)

print(add_of(coffee=2.99, cake=4.55, juice=3.55))