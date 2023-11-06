import datetime


class TimeSlot:

    def __init__(self, start_time, end_time):

        self.start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
        self.end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")

    def get_time_slot(self):
        return (self.start_time, self.end_time)

    def comparator(self, b):

        if self.timeslot.end_time < b.timeslot.end_time:
            return -1
        else:
            return 0


