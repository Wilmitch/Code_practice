#!/usr/bin/python3
class Recipe:
    def __init__(self, dish, contents, time):
        self.dish = dish
        self.contents = contents
        self.time = time
    def prepare(self):
        print("The " + self.dish + " uses " + str(self.contents) + " and takes " + str(self.time) + " mins to prepare")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato", "chicken"], 45)
masala = Recipe("Chips masala", ["chopped potatoes", "masala", "tomatoes"], 55)

print(pizza.contents)
print(masala.contents)
print(pizza.prepare())
