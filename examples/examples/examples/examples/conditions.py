# استفاده از شرط‌ها (if, elif, else)

# مثال 1: تشخیص نمره
score = float(input("نمره خود را وارد کنید (0-20): "))

if score >= 18:
    print("وضعیت: عالی ✨")
elif score >= 15:
    print("وضعیت: خیلی خوب 👍")
elif score >= 12:
    print("وضعیت: خوب ✅")
elif score >= 10:
    print("وضعیت: قبول ⚠️")
else:
    print("وضعیت: مردود ❌")

# مثال 2: تشخیص زوج یا فرد
print("\n--- تشخیص زوج یا فرد ---")
number = int(input("یک عدد وارد کنید: "))

if number % 2 == 0:
    print(f"عدد {number} زوج است")
else:
    print(f"عدد {number} فرد است")
