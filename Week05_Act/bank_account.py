class BankAccount_jcs:
    def __init__(self_jcs, account_name_jcs, balance_jcs):
        self_jcs.account_name_jcs = account_name_jcs
        self_jcs.balance_jcs = balance_jcs
    
    def deposit_jcs(self_jcs, amount_jcs):
        self_jcs.balance_jcs += amount_jcs
        print("Deposit successful")
    
    def withdraw_jcs(self_jcs, amount_jcs):
        if amount_jcs <= self_jcs.balance_jcs:
            self_jcs.balance_jcs -= amount_jcs
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_jcs(self_jcs):
        print("Balance:", self_jcs.balance_jcs)

account_jcs = BankAccount_jcs("Juan", 5000)
account_jcs.deposit_jcs(1000)
account_jcs.withdraw_jcs(2000)
account_jcs.display_balance_jcs()
