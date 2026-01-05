# Write a program to find the sum of the series :
# s=1+x+x ²+x ³+x ⁴…+x ⁿ
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

# Read the value of x and n
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Initialize sum
total = 1   # because the series starts with 1

# Loop to calculate the sum
for i in range(1, n + 1):
    total = total + (x ** i)

# Display the result
print("Sum of the series is:", total)
