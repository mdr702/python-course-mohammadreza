"""
کار با تاریخ و زمان - کتابخانه datetime
"""

from datetime import datetime, date, time, timedelta
import persian  # برای تاریخ شمسی (نصب: pip install persian)

def datetime_basics():
    """مبانی datetime"""
    now = datetime.now()
    
    print('📅 تاریخ و زمان حال:')
    print(f'  کامل: {now}')
    print(f'  سال: {now.year}')
    print(f'  ماه: {now.month}')
    print(f'  روز: {now.day}')
    print(f'  ساعت: {now.hour}:{now.minute}:{now.second}')
    
    # فقط تاریخ
    today = date.today()
    print(f'\n📆 امروز: {today}')
    
    # فقط زمان
    current_time = now.time()
    print(f'⏰ زمان: {current_time}')

def date_formatting():
    """فرمت‌دهی تاریخ"""
    now = datetime.now()
    
    print('\n📝 فرمت‌های مختلف:')
    print(f'  YYYY-MM-DD: {now.strftime("%Y-%m-%d")}')
    print(f'  DD/MM/YYYY: {now.strftime("%d/%m/%Y")}')
    print(f'  Month DD, YYYY: {now.strftime("%B %d, %Y")}')
    print(f'  Weekday: {now.strftime("%A")}')
    print(f'  Time (24h): {now.strftime("%H:%M:%S")}')
    print(f'  Time (12h): {now.strftime("%I:%M %p")}')
    print(f'  Full: {now.strftime("%Y-%m-%d %H:%M:%S")}')

def date_calculations():
    """محاسبات زمانی"""
    now = datetime.now()
    
    print('\n🧮 محاسبات زمانی:')
    
    # افزودن به تاریخ
    tomorrow = now + timedelta(days=1)
    next_week = now + timedelta(weeks=1)
    next_month = now + timedelta(days=30)
    two_hours_later = now + timedelta(hours=2)
    
    print(f'  فردا: {tomorrow.strftime("%Y-%m-%d")}')
    print(f'  هفته بعد: {next_week.strftime("%Y-%m-%d")}')
    print(f'  ۳۰ روز بعد: {next_month.strftime("%Y-%m-%d")}')
    print(f'  ۲ ساعت بعد: {two_hours_later.strftime("%H:%M")}')
    
    # تفریق تاریخ‌ها
    birthday = datetime(1990, 5, 15)
    age = now - birthday
    
    print(f'\n🎂 محاسبه سن:')
    print(f'  تاریخ تولد: {birthday.strftime("%Y-%m-%d")}')
    print(f'  سن: {age.days // 365} سال')
    print(f'  سن به روز: {age.days} روز')
    print(f'  سن به ثانیه: {age.total_seconds():.0f} ثانیه')

def age_calculator():
    """ماشین حساب سن با ورودی کاربر"""
    print('\n🧮 ماشین حساب سن')
    print('-' * 30)
    
    try:
        birth_str = input('تاریخ تولد (سال-ماه-روز): ')
        birth_date = datetime.strptime(birth_str, '%Y-%m-%d')
        
        now = datetime.now()
        
        if birth_date > now:
            print('❌ تاریخ تولد نمی‌تواند در آینده باشد!')
            return
        
        # محاسبه دقیق سن
        years = now.year - birth_date.year
        months = now.month - birth_date.month
        days = now.day - birth_date.day
        
        if days < 0:
            months -= 1
            # تعداد روزهای ماه قبل
            previous_month = now.replace(day=1) - timedelta(days=1)
            days += previous_month.day
        
        if months < 0:
            years -= 1
            months += 12
        
        print(f'\n🎂 سن شما: {years} سال, {months} ماه, {days} روز')
        
        # تولد بعدی
        next_birthday = datetime(now.year, birth_date.month, birth_date.day)
        if next_birthday < now:
            next_birthday = datetime(now.year + 1, birth_date.month, birth_date.day)
        
        days_to_birthday = (next_birthday - now).days
        print(f'🎈 تا تولد بعدی: {days_to_birthday} روز')
        
        # روز هفته تولد
        weekday_names = ['دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه', 'شنبه', 'یک‌شنبه']
        weekday = birth_date.weekday()
        print(f'📅 روز تولد: {weekday_names[weekday]}')
        
    except ValueError:
        print('❌ فرمت تاریخ اشتباه است! (استفاده از: 1990-05-15)')

if __name__ == '__main__':
    datetime_basics()
    date_formatting()
    date_calculations()
    age_calculator()
