# Program to print first 20 Fibonacci numbers
# Author: Aayushi Choudhury
# Class: XI (Science)

# First two Fibonacci numbers
a = 0
b = 1

print("First 20 Fibonacci numbers:")

for i in range(20):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
