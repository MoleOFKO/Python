weight = float(input("Please Enter the Weight in kg : "))
height = float(input("Please Enter the Height in m : "))

BMI = weight / (height ** 2)

if BMI >= 30:
    print("Obese")
elif BMI >=25 and BMI <=29.9:
    print("Overweight")
elif BMI >= 18.5 and BMI <= 24.5:
    print("Normal Weight")
elif BMI < 18.5:
    print("Under Weight")
else:
    print("Weight Invalid")