# Conditional Statements | دستورات شرطی

print("=== Grade System | سیستم نمره‌دهی ===")
score = float(input("Enter score (0-20) | نمره (0-20): "))

if score >= 18:
    result = "Excellent | عالی"
elif score >= 15:
    result = "Very Good | خیلی خوب"
elif score >= 12:
    result = "Good | خوب"
elif score >= 10:
    result = "Pass | قبول"
else:
    result = "Fail | مردود"

print(f"Result | نتیجه: {result}")

print("\n=== Even or Odd | زوج یا فرد ===")
number = int(input("Enter a number | عدد: "))

if number % 2 == 0:
    print(f"{number} is even | زوج است")
else:
    print(f"{number} is odd | فرد است")

print("\n=== Age Group | گروه سنی ===")
age = int(input("Enter age | سن: "))

if age < 13:
    group = "Child | کودک"
elif age < 20:
    group = "Teenager | نوجوان"
elif age < 60:
    group = "Adult | بزرگسال"
else:
    group = "Senior | سالمند"

print(f"Age group | گروه سنی: {group}")
