# 4.	Write a program that inputs a student’s marks in three subjects (out of 100) and prints the percentage marks.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

print(f"Percentage marks: {percentage}%")