#!/usr/bin/python3
bill = 156.00

tax = 17

total_tax = (bill * tax) / 100

print("The Total tax is : ", total_tax)

def calculate_tax(bill, tax):
    return (bill * tax) / 100

print("The total tax is : ", calculate_tax(bill, tax))