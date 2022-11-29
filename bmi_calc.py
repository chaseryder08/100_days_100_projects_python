weight = input("Enter your body weight in pounds : ")
weight = int(weight)
kg_conversion = int(weight * 0.453592)
print("You weigh " + str(kg_conversion) + " kg")

height = input("Enter your height in meters : ")
print("You are " + str(height) + " meters tall.")
height = float(height)

bmi_conversion = int(kg_conversion) / (height ** 2)

bmi = round(bmi_conversion)

if bmi < 18.5: 
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")

#if bmi_conversion < 18.5:
    #print(f"Your BMI is {bmi_conversion}, you are underweight")
#elif bmi_conversion >= 18.5


#print(bmi_conversion)