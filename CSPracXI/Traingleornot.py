# Input three angles and determine if they form a triangle or not.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("The angles form a triangle.")
else:
    print("The angles do not form a triangle.")