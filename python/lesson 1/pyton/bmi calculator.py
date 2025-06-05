# BMI Calculator

# Input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result based on BMI value
if bmi < 16:
    print(f"Your BMI is {bmi:.2f} \nYou are severely underweight.")
elif bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} \nYou are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} \nYou are healthy.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} \nYou are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f} \nYou are obese.")
else:
    print(f"Your BMI is {bmi:.2f} \nYou are severely obese.")
