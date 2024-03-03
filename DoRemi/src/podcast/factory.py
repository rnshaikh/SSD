import conf

from src.podcast.free_podcast_plan import FreePodcastPlan
from src.podcast.personal_podcast_plan import PersonalPodcastPlan
from src.podcast.premium_podcast_plan import PremiumPodcastPlan


def podcast_factory(plan_type):

    plan = {
        conf.FREE: FreePodcastPlan,
        conf.PERSONAL : PersonalPodcastPlan,
        conf.PREMIUM : PremiumPodcastPlan
    }

    return plan[plan_type]()