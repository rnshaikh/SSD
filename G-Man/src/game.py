
from src.position import Position
from src.service import PowerService


class Game:

    def __init__(self):
        self._source = None
        self._destination = None
        self._power_service = None

    def add_source(self, x, y, dire):
        self._source = Position(x, y, dire)

    def add_destination(self, x, y):
        self._destination =Position(x, y)
        
    def print_out(self):
        self._power_service = PowerService(self._source)
        power = self._power_service.calculate(self._destination)
        print("POWER ", power)

