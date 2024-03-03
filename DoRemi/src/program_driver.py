import conf

from src.streaming_app import Subscription


class ProgramDriver:

    def __init__(self):
        self._subscription = Subscription()

    @property
    def subscription(self):
        return self._subscription
        
    def start_subscription_handler(self, date):
        error = self.subscription.start_subscription(date)
        if error:
            print(error)
    
    def add_subscription_handler(self, category, plan_type):
        error = self.subscription.add_streaming_subscription(category, plan_type)
        if error:
            print(error)

    def add_topup_handler(self, plan_type, no_of_month):
        error = self.subscription.add_top_up_subscription(plan_type, no_of_month)
        if error:
            print(error)

    def print_renewal_info_handler(self):
        ans, cost, error = self.subscription.get_renewal_info()
        if error:
            print(error)
            return

        for key in ans:
            print(conf.RENEWAL_REMINDER_STR.format(category=key, date=ans[key]))

        print(conf.RENEWAL_AMOUNT_STR.format(cost=cost))


    def parse_row(self, row):

        row = row.split(" ")
        row = self.format_params(row)
        command, params = row[conf.INIT_ZERO], row[conf.INIT_ONE:]
        if not params:
            getattr(self, conf.COMMANDS[command])()
        else:
            getattr(self, conf.COMMANDS[command])(*params)

    
    def parse_file(self, file_path):

        with open(file_path, 'r') as fobj:
            for row in fobj:
                self.parse_row(row)
        
    @staticmethod
    def format_params(row):
        ans = []
        for param in row:
            param = param.strip()
            try:
                param = int(param)
                ans.append(param)
            except:
                ans.append(param)
        return ans
