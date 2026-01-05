# Write a python script to print the following pattern
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School
# Number of rows
rows = 4

for i in range(1, rows + 1):
    num = 1
    for j in range(i):
        print(num, end="    ")
        num += 2
    print()
