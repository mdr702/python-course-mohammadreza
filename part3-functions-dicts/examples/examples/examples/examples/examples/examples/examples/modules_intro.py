# Modules | ماژول‌ها

import math
from datetime import datetime
import random

# Using math module | استفاده از ماژول math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")
print(f"Factorial of 5: {math.factorial(5)}")

# Using datetime | استفاده از datetime
now = datetime.now()
print(f"Current time: {now}")
print(f"Today's date: {now.date()}")

# Using random | استفاده از random
print(f"Random number (1-100): {random.randint(1, 100)}")
colors = ["red", "blue", "green", "yellow"]
print(f"Random color: {random.choice(colors)}")
