# act3_grade.py
score = int(input("Enter score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 75:
    grade = "C"
else:
    grade = "Failed"

print(f"Grade: {grade}")
