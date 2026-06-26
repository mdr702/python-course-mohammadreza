"""
کار با فایل‌ها در پایتون
File I/O Operations
"""

import os
import json

def create_sample_files():
    """ایجاد فایل‌های نمونه"""
    
    # 1. نوشتن ساده
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write('سلام دنیا!\n')
        f.write('این خط دوم است.\n')
        f.write('پایتون عالیه! 🐍\n')
    
    # 2. نوشتن لیست
    names = ['علی', 'سارا', 'رضا', 'مریم']
    with open('names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(f'{name}\n')
    
    # 3. نوشتن دیکشنری به JSON
    data = {
        'name': 'محمد',
        'age': 25,
        'skills': ['Python', 'JavaScript']
    }
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print('✅ فایل‌های نمونه ایجاد شدند!')

def read_files():
    """خواندن فایل‌ها"""
    
    # 1. خواندن کل فایل
    with open('sample.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print('📄 محتوای فایل:')
        print(content)
    
    # 2. خواندن خط به خط
    print('\n📖 خواندن خط به خط:')
    with open('names.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(f'  - {line.strip()}')
    
    # 3. خواندن JSON
    print('\n📊 خواندن JSON:')
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"  نام: {data['name']}")
        print(f"  سن: {data['age']}")
        print(f"  مهارت‌ها: {', '.join(data['skills'])}")

def file_operations():
    """عملیات مختلف روی فایل"""
    
    # بررسی وجود فایل
    if os.path.exists('sample.txt'):
        print('✅ فایل sample.txt وجود دارد')
        
        # اطلاعات فایل
        size = os.path.getsize('sample.txt')
        print(f'📏 حجم فایل: {size} بایت')
        
        # تغییر نام
        # os.rename('sample.txt', 'sample_backup.txt')
        
        # حذف فایل (باز کردن کامنت برای حذف)
        # os.remove('sample_backup.txt')
    else:
        print('❌ فایل وجود ندارد')

if __name__ == '__main__':
    create_sample_files()
    read_files()
    file_operations()
