# Write a program to calculate and print the roots of a quadratic equation ax²+bx+c=0.(a≠0)
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

import cmath
def calculate_roots(a, b, c):
    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    
    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    
    return root1, root2