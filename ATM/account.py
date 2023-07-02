import json
from card import Card
from customer import Customer


class Account:

    def __init__(self, customer, account_no, card, amount):

        self.customer = customer
        self.account_no = account_no
        self.card = card
        self.amount = amount

    def enquiry(self):
        print("account no: %s, customer_name:%s, amount:%s" %(self.account_no, self.customer.name, self.amount))

    def add_cash(self, amount):
        self.amount += amount
        self.enquiry()

    def debit_cash(self, amount):
        self.amount -= amount
        self.enquiry()

    def check_amount_enough(self, amount):
        if self.amount < amount:
            raise Exception("Not enough cash in your account")

class Bank:
    def __new__(cls):
        if hasattr(cls, 'instance'):
            return cls.instance

        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.hash_map = {}
        self.prepare_bank()

    def add_account(self, account):
        self.hash_map[account.account_no] = account

    def get_account_by_card(self, card_no):
        for key in self.hash_map:
            if self.hash_map[key].card.no == card_no:
                return self.hash_map[key]
        raise Exception("Invalid Account")

    def get_account_by_no(self, acc_no):
        account = self.hash_map.get(acc_no, None)
        if not account:
            raise Exception("Invalid Account")
        return account

    def prepare_bank(self):
        with open('./customers.json') as f:
            customers_obj = json.loads(f.read())
            customers = customers_obj["customers"]
            print("customers", customers)

            for cust in customers:
                card_ = Card(cust['account']['card']['no'],
                             cust['account']['card']['cvv'],
                             cust['account']['card']['expiry'])
                cust_ = Customer(card_)
                account_ = Account(cust_, cust['account']['account_no'], card_, cust['account']['amount'])
                self.add_account(account_)





