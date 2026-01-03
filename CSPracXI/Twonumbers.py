# Write a program that reads two numbers and an arithmetic operator and displays the computed result.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
operator = input("Enter an arithmetic operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator."

print("Result:", result)
