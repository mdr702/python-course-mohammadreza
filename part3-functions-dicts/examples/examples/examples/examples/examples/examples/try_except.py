# Error Handling | مدیریت خطا

# Basic try/except | try/except پایه
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")

# Multiple exceptions | چند خطا
try:
    numbers = [1, 2, 3]
    index = int(input("\nEnter index (0-2): "))
    result = numbers[index]
    print(f"Value at index {index}: {result}")
except ValueError:
    print("Please enter a valid number")
except IndexError:
    print("Index out of range")

# With else and finally | با else و finally
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Program finished")
