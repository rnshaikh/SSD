import conf


class Coupon:

    def __init__(self, name, discount, min_programme, min_purcased_cost):

        self._name = name
        self._discount = discount/conf.HUNDRED
        self._min_programme = min_programme
        self._min_purcased_cost = min_purcased_cost

    @property
    def name(self):
        return self._name
    
    @property
    def discount(self):
        return self._discount

    @property
    def min_programme(self):
        return self._min_programme

    @property
    def min_purcased_cost(self):
        return self._min_purcased_cost

