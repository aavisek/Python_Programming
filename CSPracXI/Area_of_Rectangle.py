# Write a program that accepts the length and breadth of the rectangle and calculates its area.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

def calculate_area(length, breadth):
    return length * breadth

if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        area = calculate_area(length, breadth)
        print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Please enter valid numerical values for length and breadth.")
