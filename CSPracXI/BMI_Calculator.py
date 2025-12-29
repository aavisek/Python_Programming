# Write a program that accepts weight in Kg and height in meters and calculate the BMI.
# Author: Aayushi Choudhury
# Class: XI (Science)
# Aster Public School

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if height <= 0:
            print("Height must be greater than zero.")
        else:
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("Category: Underweight")
            elif bmi < 25:
                print("Category: Normal weight")
            elif bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")

    except ValueError:
        print("Please enter valid numerical values for weight and height.")
