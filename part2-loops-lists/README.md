# Python Part 2 – Loops & Lists | پایتون بخش دوم – حلقه‌ها و لیست‌ها

**Author | نویسنده:** Mohammadreza | محمدرضا

---

## Introduction | مقدمه

**English:**  
In this part, you will learn how to repeat actions using loops and how to store multiple items using lists.

**فارسی:**  
در این بخش یاد می‌گیری چطور کارها را با حلقه‌ها تکرار کنی و چطور چندین آیتم را با لیست‌ها ذخیره کنی.

**Topics | سرفصل‌ها:**
- `for` loop | حلقه for
- `while` loop | حلقه while
- `range()` function | تابع range
- Lists | لیست‌ها
- List methods | متدهای لیست
- Loop over lists | پیمایش لیست با حلقه
- Nested loops | حلقه‌های تو در تو

---

## 1. `for` Loop | حلقه for

**English:**  
The `for` loop is used to iterate over a sequence (like a string, list, or range).

**فارسی:**  
حلقه `for` برای پیمایش یک دنباله (مثل رشته، لیست یا range) استفاده می‌شود.

### Example | مثال:

```python
# Loop through a list | پیمایش یک لیست
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a string | پیمایش یک رشته
for letter in "Python":
    print(letter)

# Loop through a range | پیمایش یک بازه اعداد
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
