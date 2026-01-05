# Write a program to read an integer>1000 and reverse the number.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

number = int(input("Enter an integer greater than 1000: "))

reverse = 0

while number > 0:
    digit = number % 10        # get the last digit
    reverse = reverse * 10 + digit
    number = number // 10      # remove the last digit

print("Reversed number:", reverse)
