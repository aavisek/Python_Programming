# Write a program to input a number and print its square if it is odd, otherwise print its square root.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

num = int(input("Enter a number: "))
if num % 2 != 0:
    print("The square of the number is:", num ** 2)
else:
    print("The square root of the number is:", num ** 0.5)  
    