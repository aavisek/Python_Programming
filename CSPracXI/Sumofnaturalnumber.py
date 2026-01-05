# Write a program to print the sum of natural numbers between 1 to 7. Print the sum progressively i.e. after adding each natural number, a print sum so far.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School
sum_so_far = 0
for i in range(1, 8):
    sum_so_far += i
    print(f"After adding {i}, sum so far is: {sum_so_far}")
    
    
