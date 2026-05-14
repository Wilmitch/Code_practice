#!/usr/bin/python3
class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Supervisor(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chef(Employees):
    def leave_days(self, days):
        return "May i take " + str(days) + " days for my annual leave?"

adrian = Supervisor("Adrian", "W", "2442")
emily = Chef("Emily", "F")
jane = Chef("Angela", "K")

print(emily.leave_days(6))
print(adrian.password)
print(jane.name)