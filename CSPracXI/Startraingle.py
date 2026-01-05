# Write a program to create a triangle of stars using a nested loop.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end='')
        print()  # Move to the next line after each row
        
rows = int(input("Enter the number of rows for the triangle: "))
print_triangle(rows)
