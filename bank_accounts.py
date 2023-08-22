class FailedException(Exception):
    pass



class BankAccount:
    def __init__(self, account_name, initial_deposite):
        self.account_name       = account_name
        self.account_balance    = int(initial_deposite)
        self.create()

    def create(self):
        print(f"\nYour account has been created successfully!! 🎉\naccount_name: {self.account_name}\naccount_balance: {self.account_balance:.2f}\n");
        

    def get_balance(self):
        print(f"\nDear {self.account_name}\nyour account balance is now = #{self.account_balance:.2f}")

    def deposite(self,amount):
        self.account_balance += int(amount);
        print(f'\nDeposite complete 😊😊😊');
        self.get_balance()

    def transaction_checker(self,amount):
        if self.account_balance >= amount:
            return
        else:
            raise FailedException(f"\nTRANSACTION ERROR:\n {self.account_name} You only have a balance of {self.account_balance:.2f}")

    def withdraw(self,amount):
        try:
            self.transaction_checker(amount)
            self.account_balance = self.account_balance - amount
            print(f"\nwithrawal of {amount} successful");
            self.get_balance();
        except FailedException as error:
            print(error)
           

    def transfer(self, amount, account):
        try:
            print(f'\n**********\n\nBeginning Transfer... 🚀')
            self.transaction_checker(amount)
            self.withdraw(amount);
            account.deposite(amount)
            self.get_balance();
            print(f"Transaction complete!! ✔✔✔\n\n**********")
        except FailedException as error:
            print(error)
            print('Transfer Interupted ❌❌❌')



