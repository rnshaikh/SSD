import conf
from src.plan import Plan
from src.music.factory import music_factory
from src.video.factory import video_factory
from src.podcast.factory import podcast_factory
from src.topup.factory import device_factory

class PlanBuilder:

    streaming = {
        conf.MUSIC : music_factory,
        conf.VIDEO : video_factory,
        conf.PODCAST: podcast_factory
    }

    def __init__(self, plan_type, category=None):
        self._plan = self.set_plan(plan_type, category)

    @property
    def plan(self):
        return self._plan

    def get_streaming_plan(self, category, plan_type):
        plan_obj = self.streaming.get(category)(plan_type)
        return plan_obj
        
    def get_topup_plan(self, plan_type):

        plan_obj = device_factory(plan_type)
        return plan_obj

    def set_plan(self, plan_type, category):

        if category:
            return self.get_streaming_plan(category, plan_type)
        else:
            return self.get_topup_plan(plan_type)




