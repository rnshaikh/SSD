

class Event:

    def __init__(self, name, timeslot):

        self.name = name
        self.participant = set()
        self.timeslot = timeslot

    def get_name(self):
        return self.name

    def get_participants(self):
        return self.participant

    def add_participants(self, user):
        self.participant.add(user)

    def comparator(self, b):

        if self.timeslot.end_time < b.timeslot.end_time:
            return -1
        else:
            return 0

    def set_timeslot(self, timeslot):
        self.timeslot = timeslot

