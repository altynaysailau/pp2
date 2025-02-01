class bankacc:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit succesful! your new balance: {self.balance}tg")
        else:
            print(f"deposit amount must be positive or you did not add money")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"you have not enough money lol")
        elif amount<=0:
            print(f"it must be positive")
        else:
            self.balance-=amount
            print(f"withdrawal successful! your new balance: {self.balance}tg")
            #print('unavailable sum of withdraw ')
name = bankacc("Altynay", 100000)
print(f"Account owner: {name.owner}")
print(f"Initial balance: {name.balance}tg")

name.deposit(0)
name.withdraw(50000)



        