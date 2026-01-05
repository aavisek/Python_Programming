# Write a program to calculate and print the roots of a quadratic equation ax²+bx+c=0.(a≠0)
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

import cmath
a = float(input("Enter coefficient a (a ≠ 0): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
# The cmath module is used to handle complex roots as well.
