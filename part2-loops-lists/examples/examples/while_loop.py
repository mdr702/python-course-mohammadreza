# مثال‌های حلقه while

print("=== 1. شمارش از 1 تا 5 ===")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1  # این خط رو حتما باید بنویسی، وگرنه حلقه تا بینهایت ادامه پیدا می‌کنه!

print("\n=== 2. جمع اعداد 1 تا 10 ===")
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(f"جمع اعداد 1 تا 10 برابر است با: {total}")

print("\n=== 3. استفاده از break (خروج از حلقه) ===")
num = 0
while True:  # این یک حلقه بی‌نهایت است
    print(num)
    num += 1
    if num == 5:
        break  #当 num 等于 5 时، 我们从循环中退出

print("\n=== 4. استفاده از continue (پریدن از یک دور) ===")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # از چاپ عدد 3 صرف نظر کن
    print(i)
