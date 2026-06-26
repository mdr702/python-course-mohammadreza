"""
سیستم یادآوری با ذخیره‌سازی در JSON
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict

class Reminder:
    """کلاس یادآوری"""
    def __init__(self, title: str, due_date: datetime, priority: str = 'متوسط'):
        self.title = title
        self.due_date = due_date
        self.priority = priority  # زیاد، متوسط، کم
        self.created_at = datetime.now()
        self.is_done = False
    
    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'due_date': self.due_date.isoformat(),
            'priority': self.priority,
            'created_at': self.created_at.isoformat(),
            'is_done': self.is_done
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        reminder = cls(data['title'], datetime.fromisoformat(data['due_date']), data['priority'])
        reminder.created_at = datetime.fromisoformat(data['created_at'])
        reminder.is_done = data['is_done']
        return reminder
    
    def __str__(self):
        status = '✅' if self.is_done else '⏳'
        days_left = (self.due_date - datetime.now()).days
        return f"{status} {self.title} - {self.priority} - {days_left} روز باقی"

class ReminderManager:
    """مدیریت یادآوری‌ها"""
    
    def __init__(self, filename: str = 'data/reminders.json'):
        self.filename = filename
        self.reminders: List[Reminder] = []
        self.load()
    
    def load(self):
        """بارگذاری از فایل"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.reminders = [Reminder.from_dict(item) for item in data]
                print(f'✅ {len(self.reminders)} یادآوری بارگذاری شد')
            except Exception as e:
                print(f'❌ خطا در بارگذاری: {e}')
                self.reminders = []
    
    def save(self):
        """ذخیره در فایل"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        try:
            data = [r.to_dict() for r in self.reminders]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f'✅ یادآوری‌ها ذخیره شد')
        except Exception as e:
            print(f'❌ خطا در ذخیره: {e}')
    
    def add_reminder(self, title: str, days: int = 0, hours: int = 0, priority: str = 'متوسط'):
        """افزودن یادآوری جدید"""
        due_date = datetime.now() + timedelta(days=days, hours=hours)
        reminder = Reminder(title, due_date, priority)
        self.reminders.append(reminder)
        self.save()
        print(f'✅ یادآوری اضافه شد: {title}')
    
    def show_reminders(self, show_done: bool = False):
        """نمایش یادآوری‌ها"""
        if not self.reminders:
            print('📭 هیچ یادآوری وجود ندارد!')
            return
        
        print('\n📋 لیست یادآوری‌ها:')
        print('=' * 50)
        
        # مرتب‌سازی بر اساس تاریخ
        sorted_reminders = sorted(self.reminders, key=lambda r: r.due_date)
        
        for r in sorted_reminders:
            if not show_done and r.is_done:
                continue
            print(f'  {r}')
        
        print('=' * 50)
    
    def get_overdue(self) -> List[Reminder]:
        """دریافت یادآوری‌های گذشته"""
        now = datetime.now()
        return [r for r in self.reminders if not r.is_done and r.due_date < now]
    
    def mark_done(self, title: str):
        """علامت‌گذاری به عنوان انجام شده"""
        for r in self.reminders:
            if r.title == title:
                r.is_done = True
                self.save()
                print(f'✅ {title} انجام شد!')
                return
        print(f'❌ یادآوری {title} پیدا نشد!')
    
    def delete_done(self):
        """حذف یادآوری‌های انجام شده"""
        before = len(self.reminders)
        self.reminders = [r for r in self.reminders if not r.is_done]
        after = len(self.reminders)
        self.save()
        print(f'🗑️ {before - after} یادآوری حذف شد')

def main():
    """منوی اصلی"""
    manager = ReminderManager()
    
    while True:
        print('\n⏰ سیستم یادآوری')
        print('1. افزودن یادآوری')
        print('2. نمایش یادآوری‌ها')
        print('3. نمایش یادآوری‌های گذشته')
        print('4. علامت‌گذاری انجام شده')
        print('5. حذف یادآوری‌های انجام شده')
        print('6. خروج')
        
        choice = input('انتخاب کنید: ')
        
        if choice == '1':
            title = input('عنوان: ')
            days = int(input('چند روز دیگر؟ (0 برای امروز): ') or '0')
            hours = int(input('چند ساعت دیگر؟ (0 برای الان): ') or '0')
            priority = input('اولویت (زیاد/متوسط/کم): ') or 'متوسط'
            manager.add_reminder(title, days, hours, priority)
        
        elif choice == '2':
            show_done = input('یادآوری‌های انجام شده را نشان دهم؟ (y/n): ').lower() == 'y'
            manager.show_reminders(show_done)
        
        elif choice == '3':
            overdue = manager.get_overdue()
            if overdue:
                print('\n⚠️ یادآوری‌های گذشته:')
                for r in overdue:
                    delay = datetime.now() - r.due_date
                    print(f'  🔴 {r.title} - {delay.days} روز تأخیر')
            else:
                print('✅ هیچ یادآوری گذشته وجود ندارد!')
        
        elif choice == '4':
            title = input('عنوان یادآوری: ')
            manager.mark_done(title)
        
        elif choice == '5':
            confirm = input('آیا مطمئن هستید؟ (y/n): ')
            if confirm.lower() == 'y':
                manager.delete_done()
        
        elif choice == '6':
            print('👋 خداحافظ!')
            break
        
        else:
            print('❌ گزینه نامعتبر!')

if __name__ == '__main__':
    main()
