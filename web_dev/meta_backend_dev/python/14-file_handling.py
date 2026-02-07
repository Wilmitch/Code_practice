#!/usr/bin/python3
# One way of file handling using open()
file = open('text.txt', mode = 'r')
data = file.readline()
print(data)
print(file.read(5))

file.close()

# Another way of file handling using with open()
try:
    with open('text.txt', 'w') as file:
        file.writelines(["\nThis a new line on this file", "\nThis line should begin on a new line"])

except Exception as e:
    print("Error encountered", e)

with open('new_file.txt', 'a') as file:
    file.writelines(["\nThis is an additional like", "\nThen this"])

  