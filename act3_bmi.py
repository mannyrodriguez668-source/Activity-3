# act3_bmi.py
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 1)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi_rounded} ({category})")
