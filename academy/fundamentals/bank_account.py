from uu import Error


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def update_balance(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        try:
            if self.balance < amount:
                raise Error("Insufficient balance!")
            else:
                self.balance = self.balance - amount
                return amount
        except Error as e:
            print(f"There was error: {e}")

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    account1 = BankAccount("Rakesh", 150)
    print(account1.update_balance(200))
    print(account1.check_balance())
    print(account1.withdraw(300))
    print(account1.check_balance())