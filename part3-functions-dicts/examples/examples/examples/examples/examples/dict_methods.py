# Dictionary Methods | متدهای دیکشنری

person = {"name": "Ali", "age": 25, "city": "Tehran", "job": "Engineer"}
print(f"Original: {person}")

# Keys and values | کلیدها و مقادیر
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Looping | پیمایش
print("\nLooping through dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Removing | حذف
removed = person.pop("city")
print(f"Removed: {removed}")
print(f"After pop: {person}")

# Copy | کپی
person_copy = person.copy()
print(f"Copy: {person_copy}")
