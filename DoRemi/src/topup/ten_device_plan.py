import conf

from src.device import Device


class TenDevice(Device):

    def __init__(self):
        super().__init__(conf.TEN_DEVICE_COST)
        self._name = conf.TEN_DEVICE

    @property
    def cost(self):
        return self._cost
        
    @property
    def name(self):
        return self._name
