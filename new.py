import sys

class Account:
    """Manages individual user account data and financial transactions."""
    def __init__(self, account_id, pin, initial_balance=0.0):
        self.account_id = account_id
        self.pin = pin
        self.balance = initial_balance

    def validate_pin(self, input_pin):
        return self.pin == input_pin

    def apply_deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def apply_withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class ATMSystem:
    """Handles the user interface and orchestration of account actions."""
    def __init__(self):
        # Simulated database of accounts
        self.registry = {
            "2025": Account("2025", "2525", 5000.00),
            "2026": Account("2026", "2626", 700.00)
        }
        self.active_session = None

    def login(self):
        print("\n--- Terminal Access: Financial Services ---")
        uid = input("Account ID: ")
        
        if uid in self.registry:
            token = input("Secure PIN: ")
            if self.registry[uid].validate_pin(token):
                self.active_session = self.registry[uid]
                print("Access Granted.")
                return True
        print("Access Denied: Invalid Credentials.")
        return False

    def execute(self):
        if not self.login():
            return

        while True:
            print(f"\nAccount: {self.active_session.account_id}")
            print(f"Available Balance: ${self.active_session.balance:,.2f}")
            print("1. Withdrawal\n2. Deposit\n3. Terminate Session")
            
            cmd = input("Selection: ")

            if cmd == '1':
                val = float(input("Amount to withdraw: "))
                if self.active_session.apply_withdrawal(val):
                    print("Transaction complete. Please collect funds.")
                else:
                    print("Transaction failed: Insufficient liquidity.")
            
            elif cmd == '2':
                val = float(input("Amount to deposit: "))
                if self.active_session.apply_deposit(val):
                    print("Funds successfully credited.")
                else:
                    print("Transaction failed: Invalid entry.")
            
            elif cmd == '3':
                print("Session ended. Secure connection closed.")
                self.active_session = None
                break

if __name__ == "__main__":
    system = ATMSystem()
    system.execute()