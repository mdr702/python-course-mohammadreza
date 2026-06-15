# Understanding __init__ and self | درک سازنده و self

class Student:
    # Class attribute | ویژگی کلاس (مشترک بین همه)
    school = "Python Academy"
    
    # Constructor - called when object is created
    def __init__(self, name, age, grade):
        print(f"Creating new student: {name}")
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
        self.grade = grade
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"School: {self.school}")
        print("---")
    
    def is_passing(self):
        return self.grade >= 10

# Creating objects (__init__ runs automatically)
student1 = Student("Ali", 20, 18)
student2 = Student("Sara", 19, 14)
student3 = Student("Reza", 21, 8)

# Showing information
student1.show_info()
student2.show_info()
student3.show_info()

# Checking if passing
print(f"{student1.name} passed: {student1.is_passing()}")
print(f"{student2.name} passed: {student2.is_passing()}")
print(f"{student3.name} passed: {student3.is_passing()}")

# Each object has its own instance attributes
print(f"\nStudent1 grade: {student1.grade}")
print(f"Student2 grade: {student2.grade}")
print(f"Student3 grade: {student3.grade}")

# But they share class attributes
print(f"\nAll students go to: {Student.school}")
