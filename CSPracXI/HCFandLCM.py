# Write a python script to input two numbers and print their HCF and LCM.
# Author: Aayushi Choudhury
# Class: XI (Science)
# School: Aster Public School

# Read two integers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function to calculate HCF and LCM
def compute_hcf_lcm(a, b):
    # Find the smaller number
    if a < b:
        smaller = a
    else:
        smaller = b

    # Find HCF using a loop
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    # Formula to calculate LCM
    lcm = (a * b) // hcf

    return hcf, lcm

# Function call
hcf, lcm = compute_hcf_lcm(num1, num2)

# Display result
print("HCF of", num1, "and", num2, "is:", hcf)
print("LCM of", num1, "and", num2, "is:", lcm)
