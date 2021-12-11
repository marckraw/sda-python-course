weight = float(input("Podaj wage [kg]: "))
height = float(input("Podaj wzrost: [m]: "))

bmi = weight / height ** 2

print(f"Your BMI: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight!")
elif bmi > 25 and bmi < 30:
    print("You are overweight!")
elif bmi > 30 and bmi < 40:
    print("You are obese!")
elif bmi > 40:
    print("Oh man... take care!")
else:
    print("Your BMI looks healthy, good job!")
