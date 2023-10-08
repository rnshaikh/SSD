from functools import cmp_to_key

from .UserManager import UserManager
from .TeamManager import TeamManager

from models.TimeSlot import TimeSlot
from models.Event import Event


class EventManager:

    def __new__(cls):
        if hasattr(cls, "instance"):
            return cls.instance
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.events = {}
        self.user_manager = UserManager()
        self.team_manager = TeamManager()

    def add_event(self, name, start_time, end_time, users, teams, rep):

        user_objs = []

        for user in users:
            user_obj = self.user_manager.get_user(user)
            if not user_obj:
                raise Exception("User %s not exists" %(user))

            flag = self.will_user_available(user_obj, start_time, end_time)
            if not flag:
                raise Exception("User %s not available" %(user))
            user_objs.append(user_obj)

        for team in teams:
            availables = 0
            team_obj = self.team_manager.get_team(team)

            if not team_obj:
                raise Exception("team %s not exists" %(team.name))

            members = team_obj.get_participants()
            for mem in members:
                flag = self.will_user_available(mem, start_time, end_time)
                if flag:
                    availables += 1

                user_objs.append(mem)

                if availables == rep:
                    break

            if availables < rep:
                raise Exception("team %s enough member is available" %(team))

        timeslot = TimeSlot(start_time, end_time)
        event = Event(name, timeslot)

        for user in user_objs:
            event.add_participants(user)
            user.add_event(event)

    def will_user_available(self, user, start_time, end_time):

        events = self.user_manager.get_events(user.name)
        order_events = sorted(events, key=cmp_to_key(Event.comparator))
        for ev in order_events:
            print("ev", ev.timeslot.start_time, ev.timeslot.end_time)

        timeslot = TimeSlot(start_time, end_time)
        dummy = Event("dummy", timeslot)

        if not len(order_events):
            return True

        if order_events[-1].timeslot.end_time < dummy.timeslot.start_time:
            return True
        return False



