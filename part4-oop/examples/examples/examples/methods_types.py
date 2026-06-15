# Types of Methods | انواع متدها در پایتون
# Instance, Class, and Static Methods

class Calculator:
    # Class attribute
    company = "Python Calc Inc"
    
    # 1. Instance Method (works with self - each object has its own)
    def __init__(self, owner):
        self.owner = owner
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def show_history(self):
        print(f"History for {self.owner}:")
        for item in self.history:
            print(f"  {item}")
    
    # 2. Class Method (works with class, not instance)
    @classmethod
    def get_company(cls):
        return cls.company
    
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name
    
    # 3. Static Method (independent, no self or cls)
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0


# Using Instance Methods
print("=== Instance Methods ===")
calc1 = Calculator("Ali")
calc2 = Calculator("Sara")

calc1.add(5, 3)
calc1.add(10, 7)
calc1.subtract(20, 5)
calc1.show_history()

print()
calc2.add(100, 200)
calc2.show_history()

# Using Class Methods
print("\n=== Class Methods ===")
print(f"Company: {Calculator.get_company()}")
Calculator.change_company("Pro Python Calc")
print(f"New Company: {Calculator.get_company()}")

# Using Static Methods
print("\n=== Static Methods ===")
print(f"Multiply 4 x 5 = {Calculator.multiply(4, 5)}")
print(f"Is 10 even? {Calculator.is_even(10)}")
print(f"Is 7 even? {Calculator.is_even(7)}")

# Static methods can be called without creating an object
print(f"Square of 6: {Calculator.multiply(6, 6)}")
