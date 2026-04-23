class BankAccount_jcs:
    def __init__(self_jcs, balance_jcs):
        self_jcs.__balance = balance_jcs

    def deposit_jcs(self_jcs, amount_jcs):
        self_jcs.__balance += amount_jcs

    def withdraw_jcs(self_jcs, amount_jcs):
        if amount_jcs <= self_jcs.__balance:
            self_jcs.__balance -= amount_jcs
        else:
            print("Insufficient funds")

    def get_balance_jcs(self_jcs):
        return self_jcs.__balance

account_jcs = BankAccount_jcs(5000)
account_jcs.deposit_jcs(1000)
account_jcs.withdraw_jcs(2000)
print("Balance_jcs:", account_jcs.get_balance_jcs())