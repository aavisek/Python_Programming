# Write a program to compute the area of square and triangle.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School
length = float(input("Enter the length of the square: "))
area_square = length * length
print("The area of the square with length", length, "is:", area_square)

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print("The area of the triangle with base", base, "and height", height, "is:", area_triangle)   

