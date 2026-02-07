#!/usr/bin/python3
class Employee:
    title = "title"
    employment_status = "e-status"

    def hello(self):
        print("Hello there")

emp1 = Employee()
print(emp1)
print(emp1.title)
print(Employee.employment_status)
print(emp1.hello())

class House:
    '''
    Docstring for House to hepl calculate the cost of construction
    '''
    num_rooms = 5
    num_baths = 2

    def cost_evaluator(self, rate):
        cost = self.num_rooms * rate
        return cost
    
house = House()
print(house.num_rooms)
print(house.num_baths)
print(House.num_rooms)
print(House.num_baths)
house.num_rooms = 7
print(house.num_rooms)
print(house.num_baths)
print(House.num_rooms)
print(House.num_baths)
House.num_rooms = 7
print(house.num_rooms)
print(house.num_baths)
print(House.num_rooms)
print(House.num_baths)
