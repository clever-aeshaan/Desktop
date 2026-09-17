weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height /100) ** 2


print("Your BMI is:", bmi)
if bmi < 18.5:
    print("you are underweight")
elif bmi < 24.9:
    print("you are normal weight")
elif bmi < 29.9:
    print("you are overweight")
else:
    print("you are obese")
    print("BMI calculation complete.")
