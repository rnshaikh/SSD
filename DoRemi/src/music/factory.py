import conf 

from src.music.free_music_plan import FreeMusicPlan
from src.music.personal_music_plan import PersonalMusicPlan
from src.music.premium_music_plan import PremiumMusicPlan


def music_factory(plan_type):

    plan = {
        conf.FREE: FreeMusicPlan,
        conf.PERSONAL : PersonalMusicPlan,
        conf.PREMIUM : PremiumMusicPlan
    }

    return plan[plan_type]()
