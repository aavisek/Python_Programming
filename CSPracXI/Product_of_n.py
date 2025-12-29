# Write a program that reads the number n and print the value of n², n³ and n⁴.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

try:
    n = int(input("Enter a number: "))
    
    n_squared = n ** 2
    n_cubed = n ** 3
    n_quartic = n ** 4

    print(f"{n} squared is: {n_squared}")
    print(f"{n} cubed is: {n_cubed}")
    print(f"{n} to the power of 4 is: {n_quartic}")

except ValueError:
    print("Please enter a valid integer.")  
