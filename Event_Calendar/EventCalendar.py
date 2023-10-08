from managers.EventManager import EventManager
from managers.UserManager import UserManager
from managers.TeamManager import TeamManager


class EventCalendar:

    def __new__(cls):
        if hasattr(cls, "instance"):
            return cls.instance
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):

        self.event_manager = EventManager()
        self.user_manager = UserManager()
        self.team_manager = TeamManager()

    def create_user(self, name, start_time, end_time):
        self.user_manager.add_user(name, start_time, end_time)

    def create_team(self, name, participants):
        self.team_manager.create_team(name, participants)

    def create_event(self, name, start_time, end_time, users, teams, rep):
        self.event_manager.add_event(name, start_time, end_time, users, teams, rep)

    def print_user(self, user):

        events = self.user_manager.get_events(user)
        for event in events:
            print("event %s name has start_time %s and end_time %s"
                  %(event.name, event.timeslot.start_time, event.timeslot.end_time))
