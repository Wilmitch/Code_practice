#!/usr/bin/python3
# str[start: stop: step] - slicing method
test_str = "reversal"
new_str = test_str[::-1]
print(test_str)
print(new_str)

# Using recursion
def str_reverse(str):
    if len(str) == 0:
        return str
    else:
        return str_reverse(str[1:]) + str[0]

print(test_str)
print(str_reverse(test_str))