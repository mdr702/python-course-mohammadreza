# Input & Output | ورودی و خروجی

# Simple input | ورودی ساده
name = input("Enter your name | نام خود را وارد کنید: ")

# Input with type conversion | ورودی با تبدیل نوع
age = int(input("Enter your age | سن خود را وارد کنید: "))

# Output | خروجی
print("\n--- Information | اطلاعات ---")
print(f"Hello {name}")
print(f"سلام {name}")

print(f"You are {age} years old")
print(f"شما {age} سال دارید")

# Calculate with input | محاسبه با ورودی
number = float(input("\nEnter a number | یک عدد وارد کنید: "))
print(f"Double | دو برابر: {number * 2}")
print(f"Square | مجذور: {number ** 2}")
