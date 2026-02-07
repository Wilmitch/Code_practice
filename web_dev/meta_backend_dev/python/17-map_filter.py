#!/usr/bin/python3
# Map function
menu = ['espresso', 'mocha', 'latte', 'cappucino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

find_coffees = map(find_coffee, menu)
print(find_coffees)
for item in find_coffees:
    print(item)

find_coffees = filter(find_coffee, menu)
print(find_coffees)
for item in find_coffees:
    print(item)