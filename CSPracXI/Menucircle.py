# Write a program to display a menu for calculating the area of the circle or perimeter of the circle.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

import math
def calculate_area(radius):
    return math.pi * radius * radius

def calculate_perimeter(radius):
    return 2 * math.pi * radius 
def main():
    print("Menu:")
    print("1. Calculate Area of Circle")
    print("2. Calculate Perimeter of Circle")
    choice = input("Enter your choice (1 or 2): ")
    
    radius = float(input("Enter the radius of the circle: "))
    
    if choice == '1':
        area = calculate_area(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
    elif choice == '2':
        perimeter = calculate_perimeter(radius)
        print(f"The perimeter of the circle with radius {radius} is: {perimeter:.2f}")
    else:
        print("Invalid choice. Please select 1 or 2.")
if __name__ == "__main__":
    main()
    