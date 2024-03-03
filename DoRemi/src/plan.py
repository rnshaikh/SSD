import conf

from abc import ABC, abstractmethod

from dateutil.relativedelta import relativedelta
from datetime import timedelta

class Plan(ABC):

    def __init__(self, month, cost):
        self._month = month
        self._cost = cost
        
    @property
    @abstractmethod
    def month(self):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass
        
    def get_renewal_date(self, date):
        renewal_date = date + relativedelta(months=self.month)
        renewal_date = renewal_date - timedelta(days=conf.REMINDER_DAY)
        return renewal_date