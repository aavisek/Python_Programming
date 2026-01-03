# Write a program to accept the year and check if it is a leap year or not.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    