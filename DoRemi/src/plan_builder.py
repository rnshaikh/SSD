import conf
from src.plan import Plan
from src.category import StreamingCategory, TopupCategory

class PlanBuilder:

    def __init__(self, category, plan_type, no_of_month=None):
        self._plan = self.set_plan(category, plan_type, no_of_month) 

    @property
    def plan(self):
        return self._plan

    def get_streaming_plan(self, category, plan_type):
        
        plan_obj = Plan(category, plan_type)
        plan_obj.month = conf.STREAMING[category][plan_type]["month"]
        plan_obj.cost = conf.STREAMING[category][plan_type]["cost"]
        plan_obj.device = conf.INIT_ONE
        return plan_obj

    def get_topup_plan(self, category, plan_type, no_of_month):

        plan_obj = Plan(category, plan_type)
        plan_obj.month = no_of_month
        plan_obj.cost = conf.TOPUP[plan_type]["cost"] * no_of_month
        plan_obj.device = conf.TOPUP[plan_type]["device"]
        return plan_obj

    def set_plan(self, category, plan_type, no_of_month):

        if category in StreamingCategory.as_list():
            return self.get_streaming_plan(category, plan_type)
        else:
            return self.get_topup_plan(category, plan_type, no_of_month)




