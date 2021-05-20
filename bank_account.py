from datetime import datetime as dt
import uuid


class Bankaccount:
    """Bank account"""
    nowdate = str

    def __repr__(self):
        return 'Pumpkin Trust'

    def __init__(self, account_name: str):
        """Constructor"""
        self.account_name = account_name
        self.uniqid = str(uuid.uuid4())
        self.balance = 0.00
        self.transactions = []

    def debit(self, x: float):
        transaction_time = dt.now().strftime('%Y.%m.%d  %H:%M:%S')
        transaction = [x, 'debit', transaction_time]
        self.transactions.append(transaction)
        transaction_name = ('Deposit ' + str(x) + ' pumpkins for ' +
                            self.account_name + ' Account at ' + transaction_time)
        print(transaction_name)
        return self.transactions

    def credit(self, x: float):
        transaction_time = dt.now().strftime('%Y.%m.%d  %H:%M:%S')
        commission = 0.001 * x
        transaction = [- (x - commission), 'credit', transaction_time]
        self.transactions.append(transaction)
        transaction_name = ('Withdraw ' + str(x + commission) + ' pumpkins ' + '(Pumpkin commission: ' +
                            str(commission) + ') from ' + self.account_name + ' Account at ' + transaction_time)
        print(transaction_name)
        return self.transactions

    def get_balance(self):
        balance_result = sum([x[0] for x in self.transactions])
        return '%.2f' % balance_result + ' pumpkins' if balance_result >= 0.00 \
            else 'Sorry, you don\'t have enough pumpkins to get the balance \n' \
                 + '( %.2f' % balance_result + ' pumpkins )'


if __name__ == "__main__":
    Goat = Bankaccount('Goat')
    Goat.debit(55)
    print(Goat.uniqid)
    Goat.credit(135)
    Goat.credit(88)
    print(Goat.get_balance())
    for n in Goat.transactions:
        print(n)
    Goat.debit(300)
    Goat.credit(100)
    for n in Goat.transactions:
        print(n)
    print(Goat.get_balance())
