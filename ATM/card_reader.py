from account import Bank

class CardReader:

    def read_card(self, atm, no):
        bank = Bank()
        account = bank.get_account_by_card(no)
        atm.account = account
        return account

