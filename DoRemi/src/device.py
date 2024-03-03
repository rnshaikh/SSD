import conf

from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self, cost):
        self._cost = cost
        
    @property
    @abstractmethod
    def cost(self):
        pass
