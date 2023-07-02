

class DepositSlot:

    def accept(self):
        pass


class CashDepositSlot(DepositSlot):

    def __init__(self):
        self.cash = None

    def accept(self, cash):
        self.cash = cash


class ChequeDepositSlot(DepositSlot):

    def __init__(self):
        self.cheque = None

    def accept(self, cheque):
        self.cheque = cheque
