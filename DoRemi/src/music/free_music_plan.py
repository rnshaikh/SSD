
import conf
from src.plan import Plan

from dateutil.relativedelta import relativedelta
from datetime import timedelta


class FreeMusicPlan(Plan):

    def __init__(self):
        super().__init__(conf.FREE_MONTH, conf.FREE_COST)
        self._name = conf.FREE

    @property
    def month(self):
        return self._month

    @property
    def cost(self):
        return self._cost
        
    @property
    def name(self):
        return self._name