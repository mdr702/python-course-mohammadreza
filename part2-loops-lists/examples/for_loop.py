# مثال‌های حلقه for

print("=== 1. پیمایش یک لیست ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n=== 2. پیمایش یک رشته ===")
for letter in "Python":
    print(letter)

print("\n=== 3. استفاده از range() ===")
for i in range(5):  # اعداد 0 تا 4
    print(i)

print("\n=== 4. range(start, stop) ===")
for i in range(2, 6):  # اعداد 2 تا 5
    print(i)

print("\n=== 5. range(start, stop, step) ===")
for i in range(1, 10, 2):  # اعداد فرد 1 تا 9
    print(i)

print("\n=== 6. شمارش معکوس ===")
for i in range(5, 0, -1):
    print(i)
