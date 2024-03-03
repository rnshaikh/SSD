import conf

from src.device import Device


class FourDevice(Device):

    def __init__(self):
        super().__init__(conf.FOUR_DEVICE_COST)
        self._name = conf.FOUR_DEVICE

    @property
    def cost(self):
        return self._cost
        
    @property
    def name(self):
        return name
