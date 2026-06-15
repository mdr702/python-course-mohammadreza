# Introduction to Classes and Objects | معرفی کلاس‌ها و اشیاء

# Simple class | کلاس ساده
class Car:
    # Class attribute | ویژگی کلاس
    wheels = 4
    
    # Constructor | سازنده
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    # Method | متد
    def start(self):
        print(f"{self.brand} is starting...")
    
    def show_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Wheels: {self.wheels}")

# Creating objects | ساخت اشیاء
car1 = Car("Toyota", "White")
car2 = Car("BMW", "Black")

# Using objects | استفاده از اشیاء
car1.show_info()
car2.show_info()

car1.start()
car2.start()

# Accessing attributes | دسترسی به ویژگی‌ها
print(f"Car1 brand: {car1.brand}")
print(f"Car2 color: {car2.color}")
print(f"All cars have {Car.wheels} wheels")
