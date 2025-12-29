# Write a program to accept the marks of five subjects and calculate the average marks
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

# Ask for marks one by one and convert them to float numbers
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Add all marks and divide by 5 to get the average
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

print("Average marks:", average)
