# Write a program to find the lowest among the three integers.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

# Get input from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

# Find the lowest number using min() function
lowest = min(num1, num2, num3)

# Display the result
print(f"The lowest integer among {num1}, {num2}, and {num3} is: {lowest}")