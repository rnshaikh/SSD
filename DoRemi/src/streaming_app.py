import conf
import datetime

from src.plan_builder import PlanBuilder
from src.validator import validate_add_top_up_subscription, validate_add_streaming_subscription

class Subscription:

    def __init__(self):
        self._date = None 
        self._is_valid = True
        self.subscriptions = {}
        self.topup = None
        self.topup_month = None

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, date):
        try:
            datetime.datetime.strptime(date, conf.DATE_FORMAT)
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
        self.date = datetime.datetime.strptime(date, conf.DATE_FORMAT).date()

    def add_streaming_subscription(self, category, plan_type):

        error =validate_add_streaming_subscription(self.is_valid, self.subscriptions, category)
        if error:
            return error

        plan_obj = PlanBuilder(plan_type, category)
        self.subscriptions[category] = plan_obj


    def add_top_up_subscription(self, plan_type, no_of_month):

        error = validate_add_top_up_subscription(self.is_valid, self.subscriptions, self.topup)
        if error:
            return error

        topup_obj = PlanBuilder(plan_type)
        self.topup_month = no_of_month
        self.topup = topup_obj


    def get_renewal_info(self):
        
        if not len(self.subscriptions):
            return {}, None, conf.SUBSCRIPTIONS_NOT_FOUND

        cost = 0
        ans = {}
        for subscription in self.subscriptions:
            renewal_date = self.subscriptions[subscription].plan.get_renewal_date(self.date)
            ans[subscription] = datetime.datetime.strftime(renewal_date, conf.DATE_FORMAT)
            cost += self.subscriptions[subscription].plan.cost
        
        if self.topup:
            cost = cost + (self.topup.plan.cost * self.topup_month)
        return ans, cost, None
