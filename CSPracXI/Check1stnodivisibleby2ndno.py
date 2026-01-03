# Write a program that accepts two numbers and check if the first number is fully divisible by the second number or not.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % num2 == 0:
    print(f"{num1} is fully divisible by {num2}.")
else:
    print(f"{num1} is not fully divisible by {num2}.")  
    
    