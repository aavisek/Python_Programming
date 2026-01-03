# Program to convert height from centimeters to feet and inches
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster PubliC School

# Step 1: Get height from user
print("=== Height Converter: CM to Feet & Inches ===")
print()
# Ask user to enter their height in centimeters
height_in_cm = float(input("Enter your height in centimeters: "))
# Step 2: Convert centimeters to inches
# Formula: 1 inch = 2.54 centimeters
# So, inches = centimeters / 2.54
total_inches = height_in_cm / 2.54
print(f"\nYour height is {total_inches:.2f} inches in total.")
# Step 3: Convert inches to feet and remaining inches
# Formula: 1 foot = 12 inches
# We divide total inches by 12 to get feet
feet = int(total_inches // 12)  # Use // for whole number division
# Calculate remaining inches using modulus (%)
# Modulus gives us the remainder after division
remaining_inches = total_inches % 12
# Step 4: Display the final result
print(f"\nFinal Result:")
print(f"Your height is {feet} feet and {remaining_inches:.2f} inches")
