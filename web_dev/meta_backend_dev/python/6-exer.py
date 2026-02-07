#!/usr/bin/python3
#num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
#Instructions
#1. Under the num_list create a new for loop and print out each value on the list in sequential order.
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
for num in num_list:
    print(num)

#2. Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition
for num in num_list:
    if num > 45:
        print(num)

#3. Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.
for num in num_list:
    if num > 45:
        print("The number {} is over 45".format(num))
    else:
        print("The number {} is under 45".format(num))

#4. Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the\
#   following: ‘Number found at position: ‘, index number
for idx, num in enumerate(num_list):
    if num == 36:
        print("Number found at position: {}".format(idx))

#5. Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
count = 0;

for idx, num in enumerate(num_list):
    count += 1
    if num == 36:
        print("Number found at position: {}".format(idx))
        break
    #count += 1
print(count)
