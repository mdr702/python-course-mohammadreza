# Introduction to Dictionaries | معرفی دیکشنری‌ها

# Creating dictionaries | ساخت دیکشنری
empty_dict = {}
person = {
    "name": "Mohammadreza",
    "age": 25,
    "city": "Tehran",
    "is_student": True
}

print(f"Empty: {empty_dict}")
print(f"Person: {person}")

# Accessing values | دسترسی به مقادیر
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Job: {person.get('job', 'Not specified')}")

# Adding and updating | اضافه و به‌روز کردن
person["job"] = "Developer"
person["age"] = 26
print(f"After update: {person}")
