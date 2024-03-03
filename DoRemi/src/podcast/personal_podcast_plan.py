import conf
from src.plan import Plan


class PersonalPodcastPlan(Plan):

    def __init__(self):
        super().__init__(conf.PERSONAL_MONTH, conf.PERSONAL_PODCAST_COST)
        self._name = conf.PERSONAL

    @property
    def month(self):
        return self._month
    
    @property
    def cost(self):
        return self._cost
        
    @property
    def name(self):
        return self._name