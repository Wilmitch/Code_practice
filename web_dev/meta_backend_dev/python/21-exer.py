#!/usr/bin/python3
class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"
    def hand_list(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book
        print(self.philosopher + " wrote the book: " + self.book)

print(MyFirstClass.index)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

'''
Manager employee system
'''
class Payslips:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = "yes"
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
        
nathan = Payslips("Nathan", "no", 3200)
roger = Payslips("Roger", "no", 4250)

print(nathan.status())
print(roger.status())

nathan.pay()
print(nathan.status())
print(roger.status())
