# Write a program to read base, width and height of parallelogram and calculate its area and perimeter.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

base = float(input("Enter the base of the parallelogram: "))
width = float(input("Enter the width of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))    
area = base * height
perimeter = 2 * (base + width)
print(f"Area of the parallelogram: {area}")
print(f"Perimeter of the parallelogram: {perimeter}")

