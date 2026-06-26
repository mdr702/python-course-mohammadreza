"""
کار با اعداد تصادفی - کتابخانه random
"""

import random
import string
import secrets

def random_basics():
    """توابع پایه random"""
    print('🎲 اعداد تصادفی:')
    print(f'  عدد صحیح ۱-۱۰: {random.randint(1, 10)}')
    print(f'  عدد اعشاری ۰-۱: {random.random():.4f}')
    print(f'  عدد اعشاری ۵-۱۰: {random.uniform(5, 10):.2f}')
    print(f'  عدد با گام ۵ (۰-۵۰): {random.randrange(0, 51, 5)}')
    print(f'  انتخاب از محدوده: {random.choice(range(1, 100))}')

def list_operations():
    """عملیات روی لیست‌ها"""
    fruits = ['سیب', 'موز', 'پرتقال', 'انگور', 'هندوانه', 'کیوی']
    
    print('\n🍎 عملیات روی لیست:')
    print(f'  لیست اصلی: {fruits}')
    print(f'  انتخاب تصادفی: {random.choice(fruits)}')
    print(f'  ۳ انتخاب بدون تکرار: {random.sample(fruits, 3)}')
    
    # به هم ریختن لیست
    shuffled = fruits.copy()
    random.shuffle(shuffled)
    print(f'  لیست به هم ریخته: {shuffled}')

def password_generator():
    """تولید رمز عبور"""
    print('\n🔑 تولید رمز عبور:')
    
    def generate_weak_password(length=6):
        """رمز ضعیف (فقط حروف کوچک)"""
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    def generate_medium_password(length=10):
        """رمز متوسط (حروف + اعداد)"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    
    def generate_strong_password(length=16):
        """رمز قوی (حروف + اعداد + نمادها)"""
        chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-='
        return ''.join(secrets.choice(chars) for _ in range(length))
    
    print(f'  ضعیف (۶ کاراکتر): {generate_weak_password()}')
    print(f'  متوسط (۱۰ کاراکتر): {generate_medium_password()}')
    print(f'  قوی (۱۶ کاراکتر): {generate_strong_password()}')

def game_guess_number():
    """بازی حدس عدد"""
    print('\n🎯 بازی حدس عدد')
    print('یک عدد بین ۱ تا ۱۰۰ حدس بزنید!')
    
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f'حدس شماره {attempts + 1}: '))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print('⚠️ عدد باید بین ۱ تا ۱۰۰ باشد!')
                continue
            
            if guess < secret:
                print('📈 عدد کوچکتر است!')
            elif guess > secret:
                print('📉 عدد بزرگتر است!')
            else:
                print(f'🎉 آفرین! در {attempts} تلاش پیدا کردید!')
                return
        
        except ValueError:
            print('❌ لطفاً یک عدد وارد کنید!')
    
    print(f'😢 تمام شد! عدد مورد نظر {secret} بود.')

def lottery_simulator():
    """شبیه‌سازی قرعه‌کشی"""
    print('\n🎰 شبیه‌سازی قرعه‌کشی')
    
    participants = ['علی', 'سارا', 'رضا', 'مریم', 'محمد', 'زهرا', 'حسین', 'فاطمه']
    
    print(f'👥 شرکت‌کنندگان: {", ".join(participants)}')
    
    # انتخاب برنده
    winner = random.choice(participants)
    print(f'🏆 برنده اصلی: {winner}')
    
    # انتخاب ۳ نفر دوم
    runners_up = random.sample([p for p in participants if p != winner], 3)
    print(f'🥈 نفرات دوم: {", ".join(runners_up)}')
    
    # شبیه‌سازی ۱۰۰ بار
    wins = {p: 0 for p in participants}
    for _ in range(100):
        winner = random.choice(participants)
        wins[winner] += 1
    
    print('\n📊 آمار ۱۰۰ بار قرعه‌کشی:')
    for participant, count in sorted(wins.items(), key=lambda x: x[1], reverse=True):
        print(f'  {participant}: {count} بار')

if __name__ == '__main__':
    random_basics()
    list_operations()
    password_generator()
    game_guess_number()
    lottery_simulator()
