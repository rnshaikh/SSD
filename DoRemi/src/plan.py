import conf

from dateutil.relativedelta import relativedelta
from datetime import timedelta

class Plan:

    def __init__(self, category, plan_type):
        self.plan_type = plan_type
        self._month = None
        self._cost = None
        self._device = None
        self.category = category

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month
    
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost
    
    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, no):
        self._device = no

    def get_renewal_date(self, date):
        renewal_date = date + relativedelta(months=self.month)
        renewal_date = renewal_date - timedelta(days=conf.REMINDER_DAY)
        return renewal_date


