#!/usr/bin/python3
# Using items() method to retrieve key value
knights = {'gallahad': 'the dirty', 'robin': 'the coward'}
for k,v in knights.items():
    print(k, v)

# Using enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Using zip()
quizes = ['name', 'quest', 'favorite color']
answers = ['Wil', 'Following Christ', 'black']
for q, a in zip(quizes, answers):
    print("What is your {}? It is {}".format(q, a))

# Using reversed()
for i in reversed(range(1, 10, 2)):
    print(i)

# Using sorted()
basket = ['apple', 'banana', 'orange', 'apple', 'pear', 'orange']
for i in sorted(basket):
    print(i)

# Using the sorted() $ set()
for i in sorted(set(basket)):
    print(i)