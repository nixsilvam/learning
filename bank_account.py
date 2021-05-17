from datetime import datetime as dt
import uuid


class Bankaccount:
    """Bank account"""
    nowdate = dt.now().strftime('%Y.%m.%d  %H:%M:%S')

    def __repr__(self):
        return 'Pumpkin Trust'

    def __init__(self, account_name: str):
        """Constructor"""
        self.account_name = account_name
        self.uniqid = str(uuid.uuid4())
        self.balance = 0.00
        self.transactions = []

    def debit(self, x: float):
        transaction = [x, 'debit', self.nowdate]
        self.transactions.append(transaction)
        self.balance += transaction[0]
        transaction_name = ('Deposit ' + str(x) + ' pumpkins for ' + self.account_name + ' Account at ' + self.nowdate)
        print(transaction_name)
        return self.balance, self.transactions

    def credit(self, x: float):
        if self.balance >= x:
            commission = 0.001 * x
            transaction = [x - commission, 'credit', self.nowdate]
            self.transactions.append(transaction)
            self.balance -= (transaction[0])
            transaction_name = ('Withdraw ' + str(x + commission) + ' pumpkins ' + '(Pumpkin commission: ' +
                                str(commission) + ') from ' + self.account_name + ' Account at ' + self.nowdate)
            print(transaction_name)
            
        else:
            print('Sorry, you don\'t have enough pumpkins to complete the transaction')
        return self.balance, self.transactions

    def get_balance(self):
        return '%.2f' % self.balance, 'pumpkins'


if __name__ == "__main__":
    Goat = Bankaccount('Goat')
    Goat.debit(55)
    print(Goat.uniqid)
    Goat.debit(135)
    Goat.credit(88)
    print(Goat.get_balance())
    for n in Goat.transactions:
        print(n)
    Goat.credit(300)
    Goat.credit(100)
