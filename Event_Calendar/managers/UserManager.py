from models.User import User
from models.TimeSlot import TimeSlot


class UserManager:

    def __new__(cls):
        if hasattr(cls, "instance"):
            return cls.instance
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):

        self.users = {}

    def add_user(self, name, start_time, end_time):

        if name in self.users:
            raise Exception("user already present")

        time_slot = TimeSlot(start_time, end_time)
        user = User(name, time_slot)
        self.users[name] = user

    def get_events(self, name):
        user = self.users.get(name, None)
        return user.events

    def get_user(self, name):
        user = self.users.get(name, None)
        return user
