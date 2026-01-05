# Program to display first 10 Mersenne numbers
# and indicate Mersenne Prime numbers
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("First 10 Mersenne Numbers:")

for n in range(1, 11):
    mersenne = (2 ** n) - 1

    if is_prime(mersenne):
        print(mersenne, "- Prime")
    else:
        print(mersenne)
