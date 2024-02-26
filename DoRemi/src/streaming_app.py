import conf
import datetime
from src.category import StreamingCategory, TopupCategory
from src.plan_builder import PlanBuilder


class Subscription:

    def __init__(self):
        self._date = None 
        self._is_valid = True
        self.subscriptions = {}
        self.topup = None

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, date):
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
        except:
            self._is_valid = False

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date 

    def start_subscription(self, date):

        self.is_valid = date
        if not self.is_valid:
            return conf.INVALID_DATE
        self.date = datetime.datetime.strptime(date, "%d-%m-%Y").date()

    def add_streaming_subscription(self, category, plan_type):

        if not self.is_valid:
            return conf.ADD_SUBSCRIPTION_FAILED + " " + conf.INVALID_DATE
  
        if category in self.subscriptions:
            return conf.ADD_SUBSCRIPTION_FAILED + " " + conf.DUPLICATE_CATEGORY

        plan_obj = PlanBuilder(category, plan_type)
        self.subscriptions[plan_obj.plan.category] = plan_obj


    def add_top_up_subscription(self, topup, plan_type, no_of_month):

        if not self.is_valid:
            return conf.ADD_TOPUP_FAILED + " " + conf.INVALID_DATE

        if not len(self.subscriptions):
            return conf.ADD_TOPUP_FAILED + " " + conf.SUBSCRIPTIONS_NOT_FOUND

        if self.topup:
            return conf.ADD_TOPUP_FAILED + " " + conf.DUPLICATE_TOPUP

        topup_obj = PlanBuilder(topup, plan_type, no_of_month)
        self.topup = topup_obj


    def get_renewal_info(self):
        
        if not len(self.subscriptions):
            return {}, None, conf.SUBSCRIPTIONS_NOT_FOUND

        cost = 0
        ans = {}
        for subscription in self.subscriptions:
            renewal_date = self.subscriptions[subscription].plan.get_renewal_date(self.date)
            ans[self.subscriptions[subscription].plan.category] = datetime.datetime.strftime(renewal_date, "%d-%m-%Y")
            cost += self.subscriptions[subscription].plan.cost
        
        if self.topup:
            cost += self.topup.plan.cost
        return ans, cost, None
