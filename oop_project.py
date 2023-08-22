from bank_accounts import *

charles= BankAccount("charles", 5000, "savings")
david= BankAccount("david", 6000, "current")

charles.deposite(8000)
david.deposite(3000)



david.withdraw(2000)
david.transfer(10000, charles)
