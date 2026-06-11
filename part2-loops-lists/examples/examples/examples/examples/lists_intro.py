# معرفی لیست‌ها در پایتون

print("=== 1. روش‌های مختلف ساخت لیست ===")
empty_list = []  # لیست خالی
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]  # لیست مختلط

print(f"لیست اعداد: {numbers}")
print(f"لیست میوه‌ها: {fruits}")

print("\n=== 2. دسترسی به عناصر لیست ===")
print(f"اولین میوه: {fruits[0]}")
print(f"آخرین میوه: {fruits[-1]}")
print(f"دو عنصر اول: {fruits[:2]}")

print("\n=== 3. تغییر عناصر لیست ===")
fruits[1] = "blueberry"  # "banana" رو به "blueberry" تغییر بده
print(f"لیست بعد از تغییر: {fruits}")

print("\n=== 4. پیمایش لیست با حلقه ===")
for fruit in fruits:
    print(fruit)
