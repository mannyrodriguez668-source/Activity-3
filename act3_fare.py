# act3_fare.py
base_fare = float(input("Base fare (PHP): "))
distance = float(input("Distance (km): "))

total = base_fare + distance * 12.5

is_discount = input("Senior/PWD? (y/n): ").strip().lower()

if is_discount == "y":
    total = total * 0.80  # 20% discount

print(f"Total Fare: PHP {total:.2f}")
