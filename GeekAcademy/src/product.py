


class Product:

    def __init__(self, type, cost):
        self._cost = cost
        self._type = type

    @property
    def cost(self):
        return self._cost

    @property
    def type(self):
        return self._type
