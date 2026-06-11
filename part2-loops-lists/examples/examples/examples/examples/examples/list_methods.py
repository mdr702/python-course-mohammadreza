# متدهای رایج در لیست‌ها

numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"لیست اصلی: {numbers}")

# اضافه کردن به انتهای لیست
numbers.append(6)
print(f"بعد از append: {numbers}")

# اضافه کردن در جای مشخص
numbers.insert(0, 0)  # در ایندکس 0، مقدار 0 رو اضافه کن
print(f"بعد از insert: {numbers}")

# حذف یک مقدار
numbers.remove(1)  # اولین عدد 1 رو حذف کن
print(f"بعد از remove: {numbers}")

# حذف از روی ایندکس
popped_item = numbers.pop()  # آخرین عنصر رو حذف کن و برگردون
print(f"عنصر حذف شده با pop: {popped_item}")
print(f"بعد از pop: {numbers}")

# پیدا کردن ایندکس یک مقدار
index_of_5 = numbers.index(5)
print(f"ایندکس عدد 5: {index_of_5}")

# مرتب‌سازی لیست (از کوچیک به بزرگ)
numbers.sort()
print(f"بعد از sort: {numbers}")

# برعکس کردن لیست
numbers.reverse()
print(f"بعد از reverse: {numbers}")
