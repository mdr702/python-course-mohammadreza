# Python Part 3 – Functions & Dictionaries | پایتون بخش سوم – توابع و دیکشنری‌ها

**Author | نویسنده:** Mohammadreza | محمدرضا

---

## Introduction | مقدمه

**English:** In this part, you will learn how to write reusable code with functions and store data in key-value pairs using dictionaries.

**فارسی:** در این بخش یاد می‌گیری چطور کدهای قابل استفاده مجدد با توابع بنویسی و چطور داده‌ها را با دیکشنری‌ها (کلید-مقدار) ذخیره کنی.

**Topics | سرفصل‌ها:**
- Functions | توابع
- Parameters and Arguments | پارامترها و آرگومان‌ها
- Return Values | مقادیر بازگشتی
- Dictionaries | دیکشنری‌ها
- Dictionary Methods | متدهای دیکشنری
- Error Handling (try/except) | مدیریت خطا
- Modules | ماژول‌ها

---

## 1. Functions | توابع

**English:** A function is a block of reusable code that performs a specific task.

**فارسی:** تابع یک بلوک کد قابل استفاده مجدد است که کار خاصی را انجام می‌دهد.

### Defining a Function | تعریف تابع:

```python
def function_name():
    # code block
    print("Hello from function")
Calling a Function | فراخوانی تابع:
python
function_name()  # Hello from function
Example | مثال:
python
# Define | تعریف
def welcome():
    print("Welcome to Python Functions!")

# Call | فراخوانی
welcome()
Output | خروجی:

text
Welcome to Python Functions!
2. Parameters and Arguments | پارامترها و آرگومان‌ها
English: Parameters are variables in the function definition. Arguments are values passed to the function.

فارسی: پارامترها متغیرهایی در تعریف تابع هستند. آرگومان‌ها مقادیری هستند که به تابع ارسال می‌شوند.

Example | مثال:
python
def greet(name):  # name is parameter
    print(f"Hello, {name}!")

greet("Ali")  # "Ali" is argument
greet("Sara")  # "Sara" is argument
Output | خروجی:

text
Hello, Ali!
Hello, Sara!
Multiple Parameters | چند پارامتر:
python
def person_info(name, age, city):
    print(f"{name} is {age} years old from {city}")

person_info("Mohammad", 25, "Tehran")
Default Parameters | پارامترهای پیش‌فرض:
python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Hello, Guest!
greet("Reza")     # Hello, Reza!
Keyword Arguments | آرگومان‌های کلیدواژه‌ای:
python
def introduce(name, job):
    print(f"I'm {name} and I'm a {job}")

introduce(job="developer", name="Ali")
# I'm Ali and I'm a developer
3. Return Values | مقادیر بازگشتی
English: Use return to send a value back from a function.

فارسی: از return برای برگرداندن مقدار از تابع استفاده کنید.

Example | مثال:
python
def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(sum_result)  # 8
Multiple Returns | چند مقدار بازگشتی:
python
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

s, p = calculate(4, 5)
print(f"Sum: {s}, Product: {p}")  # Sum: 9, Product: 20
Function Without Return | تابع بدون return:
python
def show_message(msg):
    print(msg)
    # returns None automatically

result = show_message("Hello")
print(result)  # None
4. Dictionaries | دیکشنری‌ها
English: Dictionaries store data in key-value pairs. Keys are unique and immutable.

فارسی: دیکشنری‌ها داده‌ها را به صورت جفت‌های کلید-مقدار ذخیره می‌کنند. کلیدها یکتا و غیرقابل تغییر هستند.

Creating Dictionaries | ساخت دیکشنری:
python
# Empty dictionary | دیکشنری خالی
empty_dict = {}

# Dictionary with data | دیکشنری با داده
person = {
    "name": "Mohammadreza",
    "age": 25,
    "city": "Tehran"
}

# Using dict() constructor | با سازنده dict()
person2 = dict(name="Sara", age=30, city="Shiraz")
Accessing Values | دسترسی به مقادیر:
python
person = {"name": "Ali", "age": 25, "city": "Tehran"}

# Method 1: using key | روش اول: با کلید
print(person["name"])  # Ali

# Method 2: using get() | روش دوم: با get()
print(person.get("age"))  # 25
print(person.get("job", "Not found"))  # Not found
Adding/Updating Values | اضافه/به‌روز کردن مقادیر:
python
person = {"name": "Ali", "age": 25}

# Add new key-value | اضافه کردن
person["city"] = "Tehran"

# Update existing | به‌روز کردن
person["age"] = 26

print(person)  # {'name': 'Ali', 'age': 26, 'city': 'Tehran'}
Removing Items | حذف آیتم‌ها:
python
person = {"name": "Ali", "age": 25, "city": "Tehran"}

# Remove specific key | حذف کلید مشخص
del person["age"]

# Remove and return | حذف و برگرداندن
city = person.pop("city")
print(city)  # Tehran

# Remove last item | حذف آخرین آیتم
person.popitem()

# Clear all | پاک کردن همه
person.clear()
5. Dictionary Methods | متدهای دیکشنری
Method	Description	Example
keys()	Returns all keys	person.keys()
values()	Returns all values	person.values()
items()	Returns key-value pairs	person.items()
get(key)	Returns value or None	person.get("name")
update(dict)	Merges dictionary	person.update({"age": 30})
copy()	Returns a copy	new = person.copy()
len()	Number of items	len(person)
Looping Through Dictionaries | پیمایش دیکشنری:
python
person = {"name": "Ali", "age": 25, "city": "Tehran"}

# Loop through keys | پیمایش کلیدها
for key in person.keys():
    print(key)

# Loop through values | پیمایش مقادیر
for value in person.values():
    print(value)

# Loop through both | پیمایش هر دو
for key, value in person.items():
    print(f"{key}: {value}")
6. Error Handling (try/except) | مدیریت خطا
English: Try/except blocks prevent your program from crashing when errors occur.

فارسی: بلوک‌های try/except از کرش کردن برنامه هنگام بروز خطا جلوگیری می‌کنند.

Basic Try/Except | try/except پایه:
python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")
Multiple Exceptions | چند خطا:
python
try:
    numbers = [1, 2, 3]
    index = int(input("Enter index: "))
    result = numbers[index]
    print(result)
except ValueError:
    print("Please enter a valid number")
except IndexError:
    print("Index out of range")
Else and Finally | else و finally:
python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # Runs if no error
finally:
    print("Program finished")  # Always runs
7. Modules | ماژول‌ها
English: Modules are Python files containing functions and variables you can import.

فارسی: ماژول‌ها فایل‌های پایتونی هستند که شامل توابع و متغیرهایی هستند که می‌توانید import کنید.

Importing Modules | فراخوانی ماژول:
python
# Import entire module | فراخوانی کل ماژول
import math
print(math.sqrt(16))  # 4.0

# Import specific function | فراخوانی تابع خاص
from math import pi, sqrt
print(pi)  # 3.14159
print(sqrt(25))  # 5.0

# Import with alias | فراخوانی با نام مستعار
import datetime as dt
now = dt.datetime.now()
print(now)
Exercises | تمرین‌ها
Exercise 1 – Simple Function
English: Write a function that takes two numbers and returns their sum.
فارسی: تابعی بنویسید که دو عدد بگیرد و جمع آنها را برگرداند.

Exercise 2 – Even Checker
English: Write a function that checks if a number is even (returns True/False).
فارسی: تابعی بنویسید که بررسی کند یک عدد زوج است یا نه (True/False برگرداند).

Exercise 3 – Dictionary from Lists
English: Convert two lists (keys and values) into a dictionary.
فارسی: دو لیست (کلیدها و مقادیر) را به دیکشنری تبدیل کنید.

Exercise 4 – Student Grades
English: Create a dictionary of student grades and calculate the average.
فارسی: دیکشنری از نمرات دانشجویان بسازید و میانگین را محاسبه کنید.

Exercise 5 – Safe Division
English: Write a function that divides two numbers with try/except for division by zero.
فارسی: تابعی بنویسید که دو عدد را تقسیم کند و خطای تقسیم بر صفر را مدیریت کند.

Exercise 6 – Phone Book
English: Create a simple phone book using dictionary (add, find, delete contacts).
فارسی: یک دفترچه تلفن ساده با دیکشنری بسازید (اضافه، پیدا کردن، حذف مخاطب).

Summary | جمع‌بندی
English: In this part we learned:

✅ Defining and calling functions
✅ Parameters and arguments
✅ Return values
✅ Dictionaries and their methods
✅ Looping through dictionaries
✅ Error handling with try/except
✅ Importing and creating modules

فارسی: در این بخش یاد گرفتیم:

✅ تعریف و فراخوانی توابع
✅ پارامترها و آرگومان‌ها
✅ مقادیر بازگشتی
✅ دیکشنری‌ها و متدهای آنها
✅ پیمایش دیکشنری
✅ مدیریت خطا با try/except
✅ فراخوانی و ساخت ماژول

What's Next? | بخش بعدی
English: Next: Object-Oriented Programming (OOP) in Python

فارسی: بعدی: برنامه‌نویسی شی‌گرا در پایتون

Author | نویسنده: Mohammadreza | محمدرضا محمدی
