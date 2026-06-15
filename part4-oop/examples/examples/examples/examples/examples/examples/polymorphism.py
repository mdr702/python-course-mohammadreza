# Polymorphism in Python | چندریختی در پایتون
# Same method name, different behaviors

# Base class
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass  # To be overridden by child classes
    
    def perimeter(self):
        pass  # To be overridden by child classes
    
    def describe(self):
        return f"This is a {self.name}"


# Child class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# Child class 2
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Child class 3
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c


# Child class 4
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"
        self.side = side


# Function that demonstrates polymorphism
def print_shape_info(shape):
    print(f"Shape: {shape.describe()}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 30)


# Function to calculate total area of multiple shapes
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


# Creating different shapes
print("=== Creating Shapes ===")
rectangle = Rectangle(5, 3)
circle = Circle(4)
triangle = Triangle(3, 4, 5)
square = Square(6)

# Demonstrating polymorphism
print("\n=== Polymorphism in Action ===")
print_shape_info(rectangle)
print_shape_info(circle)
print_shape_info(triangle)
print_shape_info(square)

# All shapes in a list (polymorphic collection)
print("\n=== Collection of Shapes ===")
shapes = [rectangle, circle, triangle, square]

for shape in shapes:
    print(f"{shape.name}: Area = {shape.area():.2f}")

print(f"\nTotal area of all shapes: {total_area(shapes):.2f}")

# Another example with different types
print("\n=== Another Example: Sound of Animals ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo! Moo!"

class Duck(Animal):
    def sound(self):
        return "Quack! Quack!"

# Polymorphic function
def make_sound(animal):
    print(f"{animal.name} says: {animal.sound()}")

animals = [Dog("Rex"), Cat("Kitty"), Cow("Bessie"), Duck("Donald")]

for animal in animals:
    make_sound(animal)
