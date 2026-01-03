# Write a program to print whether a given character is an uppercase or a lowercase character or a digit or any other character.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

char = input("Enter a character: ")

if char.isupper():
    print("The character is an uppercase letter.")
elif char.islower():
    print("The character is a lowercase letter.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")
    