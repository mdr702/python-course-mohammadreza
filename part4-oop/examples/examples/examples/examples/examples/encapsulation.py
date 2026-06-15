# Encapsulation in Python | کپسوله‌سازی در پایتون
# Public, Protected, and Private members

class BankAccount:
    def __init__(self, owner, account_number, initial_balance):
        # Public attribute (accessible anywhere)
        self.owner = owner
        
        # Protected attribute (convention: _single_underscore)
        self._account_number = account_number
        
        # Private attribute (name mangling: __double_underscore)
        self.__balance = initial_balance
        
        # Private attribute
        self.__transaction_history = []
    
    # Public method - accessible to everyone
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction(f"Deposit: +{amount}")
            print(f"✅ Deposited {amount:,} Toman. New balance: {self.__balance:,}")
            return True
        else:
            print("❌ Invalid amount")
            return False
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid amount")
            return False
        elif amount > self.__balance:
            print(f"❌ Insufficient balance! You have {self.__balance:,} Toman")
            return False
        else:
            self.__balance -= amount
            self.__add_transaction(f"Withdrawal: -{amount}")
            print(f"✅ Withdrew {amount:,} Toman. New balance: {self.__balance:,}")
            return True
    
    # Getter (to access private balance)
    def get_balance(self):
        return self.__balance
    
    # Getter for transaction history
    def get_transaction_history(self):
        return self.__transaction_history.copy()  # Return a copy for safety
    
    def show_info(self):
        print(f"Owner: {self.owner}")
        print(f"Account: {self._account_number}")
        print(f"Balance: {self.__balance:,} Toman")
    
    # Private method (cannot be accessed from outside)
    def __add_transaction(self, transaction):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history.append(f"[{timestamp}] {transaction}")


# Creating account
print("=== Creating Bank Account ===")
account = BankAccount("Mohammadreza", "IR1234567890", 5000000)

# Accessing public attribute - OK
print(f"\n=== Public Access ===")
print(f"Owner: {account.owner}")

# Accessing protected attribute - Possible but not recommended
print(f"\n=== Protected Access (not recommended) ===")
print(f"Account Number: {account._account_number}")

# Accessing private attribute - ERROR!
print(f"\n=== Private Access (will fail) ===")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"❌ Error: {e}")

# Using public methods to access private data
print(f"\n=== Using Getter Methods ===")
print(f"Balance via getter: {account.get_balance():,} Toman")

# Depositing and withdrawing
print(f"\n=== Transactions ===")
account.deposit(2000000)
account.withdraw(1000000)
account.withdraw(7000000)  # This should fail (insufficient)
account.deposit(5000000)
account.withdraw(3000000)

# Show transaction history
print(f"\n=== Transaction History ===")
history = account.get_transaction_history()
for trans in history:
    print(f"  {trans}")

# Show account info
print(f"\n=== Account Info ===")
account.show_info()

# Demonstrating name mangling (not recommended, just for understanding)
print(f"\n=== Name Mangling (just for learning) ===")
print(f"Private attribute is actually stored as: {dir(account)}")
# The balance is stored as _BankAccount__balance
print(f"Can access via mangled name: {account._BankAccount__balance:,} Toman")
print("⚠️ But you should NEVER do this in real code!")
