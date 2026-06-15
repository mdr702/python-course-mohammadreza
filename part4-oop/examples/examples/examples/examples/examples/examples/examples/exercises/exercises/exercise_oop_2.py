"""
Exercise 2: Bank Account Class | تمرین ۲: کلاس حساب بانکی

Create a BankAccount class with the following:
یک کلاس BankAccount با ویژگی‌های زیر بسازید:

Attributes (ویژگی‌ها):
- account_number (شماره حساب - private)
- owner (صاحب حساب - public)
- __balance (موجودی - private)

Methods (متدها):
- deposit(amount): adds money to balance (must be positive)
- withdraw(amount): subtracts money (must have sufficient balance)
- get_balance(): returns the balance (getter)
- show_info(): prints account information
- transfer(to_account, amount): transfers money to another account

Extra (امتیازی):
- Keep transaction history (list of deposits/withdrawals)
- Add interest rate and calculate monthly interest
- Prevent negative balance

Example usage | مثال:
account1 = BankAccount("123456", "Ali", 1000000)
account2 = BankAccount("789012", "Sara", 500000)

account1.deposit(500000)
account1.withdraw(200000)
account1.transfer(account2, 300000)
print(account1.get_balance())  # Should show correct balance
account1.show_info()
"""

# Your code here | کد خود را اینجا بنویسید
