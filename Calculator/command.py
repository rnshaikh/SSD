
from abc import ABC


class Command(ABC):

    def execute(self):
        pass

    def undo(self):
        pass
