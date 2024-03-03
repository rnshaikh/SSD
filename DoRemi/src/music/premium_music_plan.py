import conf
from src.plan import Plan


class PremiumMusicPlan(Plan):

    def __init__(self):
        super().__init__(conf.PREMIUM_MUSIC_MONTH, conf.PREMIUM_MUSIC_COST)
        self._name = conf.PREMIUM

    @property
    def month(self):
        return self._month
    
    @property
    def cost(self):
        return self._cost
        
    @property
    def name(self):
        return self._name