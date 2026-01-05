# Write a program to calculate the factorial of a number.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
