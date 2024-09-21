# Subject: Data Structure and Algorithm
# Lab Activity: Python review 
# Student: Braganza, Joshua S.
# Course and Section: BS CpE 2-3
# Deadline: September 22, 2024 11:59pm


# Exercise 3:  Diamond Shape (advance topic):
# Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.
# For n = 5, the output should be:
#    *
#   ***
#  *****
#   ***
#    *
# Note: If an even number is passed, the function should return "Please provide an odd integer."

def print_diamond(n):
    if n % 2 == 0:
        return print("Please provide an odd integer.")

    mid = n // 2

    for i in range(mid + 1):
        print(' ' * (mid - i) + '*' * (2 * i + 1))

    for i in range(mid - 1, -1, -1):
        print(' ' * (mid - i) + '*' * (2 * i + 1))

n = 5
print_diamond(n)