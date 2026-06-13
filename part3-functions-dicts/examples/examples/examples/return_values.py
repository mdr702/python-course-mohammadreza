# Return Values | مقادیر بازگشتی

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

# Using return values | استفاده از مقادیر بازگشتی
result = add(5, 3)
print(f"Sum: {result}")

s, p = calculate(4, 5)
print(f"Sum: {s}, Product: {p}")

# Function without return | تابع بدون return
def show_message(msg):
    print(msg)

result = show_message("Hello")
print(f"Return value: {result}")  # None
