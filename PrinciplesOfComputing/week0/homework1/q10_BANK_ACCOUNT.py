class BankAccount:
    '''
    Class definition modeling the behavior of a simple bank account
    '''
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.cur_bal = initial_balance
        self.fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.cur_bal +=amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal
        resulting in a negative balance also deducts a penalty
        fee of 5 dollars from the balance.
        """
        if self.cur_bal - amount < 0:
            self.fees +=1
            self.cur_bal -=(amount + 5)
        else:
            self.cur_bal -=amount

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.cur_bal

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees * 5

##
### should print 10 5
##
##my_account = BankAccount(10)
##my_account.withdraw(15)
##my_account.deposit(20)
##print my_account.get_balance(), my_account.get_fees()

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print my_account.get_balance(), my_account.get_fees()
