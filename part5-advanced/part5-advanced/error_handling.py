"""
مدیریت خطاها در پایتون
Error Handling
"""

import json
import os

class CustomError(Exception):
    """خطای سفارشی"""
    pass

class BankAccount:
    """حساب بانکی با مدیریت خطا"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        """واریز وجه"""
        try:
            if amount <= 0:
                raise ValueError('مبلغ واریز باید مثبت باشد!')
            
            self.balance += amount
            self.transactions.append({
                'type': 'deposit',
                'amount': amount,
                'balance': self.balance
            })
            print(f'💰 {amount:,} تومان واریز شد. موجودی: {self.balance:,} تومان')
            
        except ValueError as e:
            print(f'❌ خطا: {e}')
        except Exception as e:
            print(f'❌ خطای ناشناخته: {e}')
    
    def withdraw(self, amount):
        """برداشت وجه"""
        try:
            if amount <= 0:
                raise ValueError('مبلغ برداشت باید مثبت باشد!')
            
            if amount > self.balance:
                raise CustomError(f'موجودی ناکافی! موجودی: {self.balance:,} تومان')
            
            self.balance -= amount
            self.transactions.append({
                'type': 'withdraw',
                'amount': amount,
                'balance': self.balance
            })
            print(f'🏦 {amount:,} تومان برداشت شد. موجودی: {self.balance:,} تومان')
            
        except ValueError as e:
            print(f'❌ خطا: {e}')
        except CustomError as e:
            print(f'❌ {e}')
        except Exception as e:
            print(f'❌ خطای ناشناخته: {e}')
        finally:
            print('📊 عملیات انجام شد.')
    
    def show_transactions(self):
        """نمایش تراکنش‌ها"""
        print('\n📋 تاریخچه تراکنش‌ها:')
        print('-' * 40)
        for t in self.transactions:
            type_persian = 'واریز' if t['type'] == 'deposit' else 'برداشت'
            print(f"  {type_persian}: {t['amount']:,} تومان - موجودی: {t['balance']:,} تومان")
        print('-' * 40)

def safe_file_read(filename):
    """خواندن امن فایل با مدیریت خطا"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f'❌ فایل {filename} پیدا نشد!')
        return None
    except PermissionError:
        print(f'❌ دسترسی به فایل {filename} وجود ندارد!')
        return None
    except Exception as e:
        print(f'❌ خطا در خواندن فایل: {e}')
        return None

def safe_json_load(filename):
    """بارگذاری امن JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'❌ فایل {filename} پیدا نشد!')
        return None
    except json.JSONDecodeError:
        print(f'❌ فایل {filename} معتبر نیست!')
        return None
    except Exception as e:
        print(f'❌ خطا: {e}')
        return None

if __name__ == '__main__':
    # تست حساب بانکی
    account = BankAccount('محمد', 100000)
    
    print('🏦 بانک محمد')
    print('-' * 30)
    
    account.deposit(50000)
    account.withdraw(30000)
    account.withdraw(200000)  # این خطا میدهد
    account.deposit(-1000)    # این خطا میدهد
    
    account.show_transactions()
    
    # تست خواندن امن فایل
    content = safe_file_read('nonexistent.txt')
    if content:
        print(content)
