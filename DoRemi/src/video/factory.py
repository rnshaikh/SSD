import conf
from src.video.free_video_plan import FreeVideoPlan
from src.video.personal_video_plan import PersonalVideoPlan
from src.video.premium_video_plan import PremiumVideoPlan



def video_factory(plan_type):
    
    plan = {
        conf.FREE: FreeVideoPlan,
        conf.PERSONAL : PersonalVideoPlan,
        conf.PREMIUM : PremiumVideoPlan
    }

    return plan[plan_type]()