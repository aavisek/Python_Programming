# Write a program to input percentage marks of a student and find the grade as per the following criterion:
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

'''
Marks                        Grade

>=90                           A
75-90                          B
60-75                          C    
Below 60                       D
'''
marks = float(input("Enter the percentage marks of the student: ")) 
if marks >= 90:
    grade = 'A'
elif 75 <= marks < 90:
    grade = 'B'
elif 60 <= marks < 75:
    grade = 'C'
else:
    grade = 'D'
print("The grade of the student is:", grade)
