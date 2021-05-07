class user:
    def __init__(self, firstName, lastName, Balance):
        self.firstName = firstName
        self.lastName = lastName
        self.Balance = Balance

    def make_deposit(self, deposit):
        self.Balance += deposit
        return self

    def make_withDrow(self, deposit):
        self.Balance -= deposit
        return self

    def printBalance(self):
        print(self.Balance)
        return self

    def transfer_money(self, other_user, amount):
        other_user.Balance += amount
        self.Balance -= amount
        return self


x = user("alaa", "ibrahim", 20)
x1 = user("naser", "ibrahim", 30)
x2 = user("lana", "ibrahim", 40)


x.make_deposit(10).make_deposit(20).make_deposit(
    10).make_withDrow(5).printBalance()
x1.make_deposit(10).make_deposit(20).make_withDrow(
    5).make_withDrow(10).printBalance()
x2.make_deposit(10).make_withDrow(5).make_withDrow(
    5).make_withDrow(10).printBalance()
x.printBalance().transfer_money(x2, 10)
x2.printBalance()
x.printBalance()
