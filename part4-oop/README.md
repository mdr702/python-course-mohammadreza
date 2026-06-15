# Python Part 4 – Object-Oriented Programming (OOP) | پایتون بخش چهارم – برنامه‌نویسی شی‌گرا

**Author | نویسنده:** Mohammadreza | محمدرضا

---

## Introduction | مقدمه

**English:** Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to organize code. Objects have properties (attributes) and behaviors (methods).

**فارسی:** برنامه‌نویسی شی‌گرا (OOP) یک پارادایم برنامه‌نویسی است که از "اشیاء" برای سازماندهی کد استفاده می‌کند. اشیاء دارای ویژگی‌ها (attributes) و رفتارها (methods) هستند.

**Topics | سرفصل‌ها:**
- Classes and Objects | کلاس‌ها و اشیاء
- Attributes | ویژگی‌ها
- Methods | متدها
- Constructor (`__init__`) | سازنده
- Inheritance | وراثت
- Encapsulation | کپسوله‌سازی
- Polymorphism | چندریختی

---

## 1. Classes and Objects | کلاس‌ها و اشیاء

**English:** A class is a blueprint. An object is an instance of a class.

**فارسی:** کلاس یک نقشه است. شی یک نمونه از کلاس است.

### Defining a Class | تعریف کلاس:

```python
class Car:
    pass
Creating an Object | ساخت شی:
python
my_car = Car()
print(type(my_car))  # <class '__main__.Car'>
Example | مثال کامل:
python
class Car:
    # Attributes | ویژگی‌ها
    brand = "Toyota"
    color = "white"
    
    # Method | متد
    def start(self):
        print("The car is starting...")

# Create object | ساخت شی
car1 = Car()
print(car1.brand)    # Toyota
print(car1.color)    # white
car1.start()         # The car is starting...
Output | خروجی:

text
Toyota
white
The car is starting...
2. The __init__ Constructor | سازنده __init__
English: The __init__ method is called automatically when an object is created. It initializes the object's attributes.

فارسی: متد __init__ زمانی که شی ساخته می‌شود، به طور خودکار فراخوانی می‌شود. ویژگی‌های شی را مقداردهی اولیه می‌کند.

Example | مثال:
python
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    
    def show_info(self):
        print(f"{self.brand} - {self.color} - {self.year}")

# Create objects with different values
car1 = Car("Toyota", "White", 2020)
car2 = Car("BMW", "Black", 2023)

car1.show_info()  # Toyota - White - 2020
car2.show_info()  # BMW - Black - 2023
Output | خروجی:

text
Toyota - White - 2020
BMW - Black - 2023
What is self? | self چیست؟
English: self refers to the current object. It's a reference to the instance itself.

فارسی: self به شی فعلی اشاره دارد. این یک ارجاع به خود نمونه است.

3. Instance vs Class Attributes | ویژگی‌های نمونه در مقابل کلاس
Type	Definition	Access
Class Attribute	Shared by all objects	ClassName.attribute
Instance Attribute	Unique to each object	self.attribute
Example | مثال:
python
class Student:
    # Class attribute (shared by all)
    school = "Python High School"
    
    def __init__(self, name, grade):
        # Instance attributes (unique to each)
        self.name = name
        self.grade = grade
    
    def show_info(self):
        print(f"{self.name} - {self.grade} - {self.school}")

# Create objects
s1 = Student("Ali", 18)
s2 = Student("Sara", 19)

s1.show_info()  # Ali - 18 - Python High School
s2.show_info()  # Sara - 19 - Python High School
4. Methods | متدها
Types of Methods | انواع متدها:
Type	Definition	Decorator
Instance Method	Works with instance	self parameter
Class Method	Works with class	@classmethod
Static Method	Independent	@staticmethod
Example | مثال:
python
class Calculator:
    # Instance method
    def add(self, a, b):
        return a + b
    
    # Class method
    @classmethod
    def description(cls):
        return "This is a calculator class"
    
    # Static method
    @staticmethod
    def multiply(a, b):
        return a * b

# Usage
calc = Calculator()
print(calc.add(5, 3))           # 8
print(Calculator.description()) # This is a calculator class
print(Calculator.multiply(4, 5)) # 20
5. Inheritance | وراثت
English: Inheritance allows a class to inherit attributes and methods from another class.

فارسی: وراثت به یک کلاس اجازه می‌دهد ویژگی‌ها و متدها را از کلاس دیگر به ارث ببرد.

Example | مثال:
python
# Parent class (base) | کلاس والد
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (derived) | کلاس فرزند
class Dog(Animal):
    def speak(self):  # Override method
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Usage
animals = [Dog("Rex"), Cat("Kitty")]
for animal in animals:
    animal.speak()

# Output:
# Rex says Woof!
# Kitty says Meow!
The super() Function | تابع super():
python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"Parent: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
    
    def show(self):
        super().show()  # Call parent method
        print(f"Age: {self.age}")

c = Child("Ali", 25)
c.show()
# Output:
# Parent: Ali
# Age: 25
6. Encapsulation | کپسوله‌سازی
English: Encapsulation hides internal data and exposes only what's necessary.

فارسی: کپسوله‌سازی داده‌های داخلی را پنهان می‌کند و فقط موارد ضروری را نشان می‌دهد.

Access Modifiers | سطح دسترسی:
Convention	Meaning
public	Accessible anywhere
_protected	Accessible in class and subclasses
__private	Accessible only in class
Example | مثال:
python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._branch = "Tehran"     # protected
        self.__balance = balance    # private
    
    # Getter (access private)
    def get_balance(self):
        return self.__balance
    
    # Setter (modify private)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

account = BankAccount("Ali", 1000000)
print(account.owner)           # Ali (public)
print(account.get_balance())   # 1000000 (via getter)
account.deposit(500000)
print(account.get_balance())   # 1500000

# This will raise an error:
# print(account.__balance)  # AttributeError
7. Polymorphism | چندریختی
English: Polymorphism allows objects of different classes to be treated as objects of a common parent class.

فارسی: چندریختی به اشیاء کلاس‌های مختلف اجازه می‌دهد به عنوان اشیاء یک کلاس والد مشترک رفتار کنند.

Example | مثال:
python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 15
# Area: 50.24
8. Magic Methods | متدهای جادویی
English: Magic methods are special methods with double underscores (dunder methods).

فارسی: متدهای جادویی متدهای خاصی با خط‌فاصله دوگانه هستند.

Magic Method	Purpose
__init__(self)	Constructor
__str__(self)	String representation
__repr__(self)	Official representation
__len__(self)	Returns length
__add__(self, other)	Addition +
Example | مثال:
python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"Book: {self.title}"
    
    def __len__(self):
        return self.pages
    
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python 101", 300)
book2 = Book("Django Guide", 250)

print(str(book1))     # Book: Python 101
print(len(book1))     # 300
print(book1 + book2)  # 550
Exercises | تمرین‌ها
Exercise 1 – Student Class
English: Create a Student class with name, age, and grade. Add a method to check if the student passed (grade >= 10).

فارسی: یک کلاس Student با نام، سن و نمره بسازید. متدی اضافه کنید که بررسی کند دانشجو قبول شده است (نمره >= 10).

Exercise 2 – Bank Account
English: Create a BankAccount class with deposit, withdraw, and show_balance methods.

فارسی: یک کلاس BankAccount با متدهای واریز، برداشت و نمایش موجودی بسازید.

Exercise 3 – Inheritance
English: Create a Vehicle parent class and Car and Motorcycle child classes with different sound methods.

فارسی: یک کلاس والد Vehicle و کلاس‌های فرزند Car و Motorcycle با متدهای صدای متفاوت بسازید.

Exercise 4 – Library System
English: Create a simple library system with Book and Member classes. Include borrow and return methods.

فارسی: یک سیستم کتابخانه ساده با کلاس‌های Book و Member بسازید. متدهای امانت گرفتن و برگرداندن را اضافه کنید.

Summary | جمع‌بندی
English: In this part we learned:

✅ Classes and objects
✅ The __init__ constructor
✅ Instance vs class attributes
✅ Methods (instance, class, static)
✅ Inheritance and super()
✅ Encapsulation (public, protected, private)
✅ Polymorphism
✅ Magic methods (__str__, __len__, __add__)

فارسی: در این بخش یاد گرفتیم:

✅ کلاس‌ها و اشیاء
✅ سازنده __init__
✅ ویژگی‌های نمونه در مقابل کلاس
✅ متدها (نمونه، کلاس، استاتیک)
✅ وراثت و super()
✅ کپسوله‌سازی (public, protected, private)
✅ چندریختی
✅ متدهای جادویی

What's Next? | بخش بعدی
English: Next: Working with Files and APIs

فارسی: بعدی: کار با فایل‌ها و APIها

Author | نویسنده: Mohammadreza | محمدرضا
