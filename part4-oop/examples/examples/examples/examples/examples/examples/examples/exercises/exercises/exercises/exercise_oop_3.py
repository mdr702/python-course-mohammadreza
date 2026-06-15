"""
Exercise 3: Inheritance - Vehicle System | تمرین ۳: وراثت - سیستم وسایل نقلیه

Create a vehicle hierarchy with the following:
یک سلسله مراتب از وسایل نقلیه با ویژگی‌های زیر بسازید:

Parent Class (کلاس والد): Vehicle
Attributes: brand, model, year, speed
Methods: accelerate(), brake(), honk()

Child Class 1 (کلاس فرزند ۱): Car
Additional attributes: doors, fuel_type
Override: honk() - "Beep Beep!"

Child Class 2 (کلاس فرزند ۲): Motorcycle
Additional attributes: has_sidecar
Override: honk() - "Honk Honk!"

Child Class 3 (کلاس فرزند ۳): Truck
Additional attributes: capacity (tons)
Override: honk() - "HOOOONK!"

Extra (امتیازی):
- Create a fleet manager that can manage multiple vehicles
- Calculate average speed of all vehicles
- Find fastest vehicle

Example usage | مثال:
car = Car("Toyota", "Camry", 2020, 180, 4, "Gasoline")
bike = Motorcycle("Honda", "CBR", 2022, 220, False)
truck = Truck("Volvo", "FH16", 2019, 120, 20)

vehicles = [car, bike, truck]
for v in vehicles:
    v.honk()
    print(f"{v.brand} {v.model}: {v.speed} km/h")
"""

# Your code here | کد خود را اینجا بنویسید
