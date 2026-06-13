# Function Parameters | پارامترهای توابع

def greet(name):
    print(f"Hello, {name}!")

def person_info(name, age, city):
    print(f"{name} is {age} years old from {city}")

def greet_default(name="Guest"):
    print(f"Hello, {name}!")

# Calling | فراخوانی
greet("Mohammadreza")
person_info("Ali", 25, "Tehran")
greet_default()
greet_default("Sara")
