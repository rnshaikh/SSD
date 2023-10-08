from models.TimeSlot import TimeSlot


class User:

    def __init__(self, name, timeslot):

        self.name = name
        self.timeslot = timeslot
        self.team = None
        self.events = set()

    def set_working_hours(self, start_time, end_time):

        time_slot = TimeSlot(start_time, end_time)
        self.timeslot = time_slot

    def set_team(self, team):
        self.team = team

    def get_name(self):
        return self.name

    def get_working_hours(self):

        return self.timeslot

    def add_event(self, event):
        self.events.add(event)

