import conf

class ProgramDiscount:


    def __init__(self, programme, discount):

        self._programme = programme
        self._discount = discount/conf.HUNDRED

    @property
    def programme(self):
        return self._programme
    

    @property
    def discount(self):
        return self._discount
    


class Membership:

    def __init__(self, name, cost):
        self._name = name
        self.discounts = {}
        self._cost = cost

    @property
    def cost(self):
        return self._cost

    def add_discounts(self, programme, discount):

        programme_discount = ProgramDiscount(programme, discount)
        self.discounts[programme.type] = programme_discount

    def get_discount(self, programme):
        discount = self.discounts[programme].programme.cost * (self.discounts[programme].discount)
        return discount


