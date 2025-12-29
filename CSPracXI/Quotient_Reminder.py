# Write a program to read two numbers and print quotient and reminder.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School
def main():
    try:
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        
        quotient = num1 // num2
        remainder = num1 % num2
        
        print(f"Quotient: {quotient}")
        print(f"Remainder: {remainder}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()