from account import Bank

class ATM:

    def __init__(self, screen, card_reader, cash_dispenser,
                cheque_deposit_slot, cash_deposit_slot, printer):
        self.amount = 0
        self.screen = screen
        self.card_reader = card_reader
        self.cash_dispenser = cash_dispenser
        self.cash_deposit_slot = cash_deposit_slot
        self.cheque_deposit_slot = cheque_deposit_slot
        self.printer = printer
        self.account = None
        bank=Bank()
        bank.prepare_bank()

    def add_cash(self, amount):
        self.amount = amount

    def add_cash_customer(self, amount):
        self.amount += amount
        self.account.add_cash(amount)

    def debit_cash(self, amount):
        if self.account.amount < amount:
            raise Exception("you dont have enough cash")

        if amount > self.amount:
            raise Exception("Not Enough Cash in atm")
        self.amount -= amount
        self.account.amount -= amount

    def detail(self):
        msg = "amount :" + str(self.amount)
        self.screen.print_(msg)

    def enquiry(self):
        self.account.enquiry()

    def transfer(self, account_no, amount):
        bank = Bank()
        transfer_account = bank.get_account_by_no(account_no)
        self.account.check_amount_enough(amount)
        self.account.debit_cash(amount)
        transfer_account.add_cash(amount)
