# Beginner-friendly prime number checker
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is not a prime number")
else:
    is_prime = True

    # Try dividing by every number from 2 up to number - 1
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
