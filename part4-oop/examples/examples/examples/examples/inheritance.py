# Inheritance in Python | وراثت در پایتون

# Parent class (Base class) | کلاس والد
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Child class 1 (Inherits from Animal)
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def show_info(self):  # Override parent method
        super().show_info()  # Call parent method
        print(f"Breed: {self.breed}")
    
    def eat(self):  # Override with different behavior
        print(f"{self.name} is eating dog food...")


# Child class 2
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def meow(self):
        print(f"{self.name} says: Meow! Meow!")
    
    def show_info(self):
        super().show_info()
        print(f"Color: {self.color}")


# Child class 3
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying...")
        else:
            print(f"{self.name} cannot fly")
    
    def show_info(self):
        super().show_info()
        print(f"Can fly: {self.can_fly}")


# Creating objects
print("=== Creating Animals ===")
dog = Dog("Rex", 3, "German Shepherd")
cat = Cat("Kitty", 2, "White")
bird = Bird("Tweety", 1, True)
penguin = Bird("Pingu", 2, False)

# Using parent class methods
print("\n=== Parent Methods ===")
dog.eat()
dog.sleep()
cat.eat()
bird.sleep()

# Using child-specific methods
print("\n=== Child Methods ===")
dog.bark()
cat.meow()
bird.fly()
penguin.fly()

# Using overridden methods
print("\n=== Overridden Methods ===")
dog.show_info()
print("---")
cat.show_info()
print("---")
bird.show_info()

# Polymorphism - treating all as Animals
print("\n=== Polymorphism ===")
animals = [dog, cat, bird, penguin]
for animal in animals:
    animal.sleep()  # All have sleep() method
