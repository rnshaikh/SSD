
from EventCalendar import EventCalendar


if __name__ == "__main__":

    event_calender = EventCalendar()

    event_calender.create_user("A", "2021-07-07T9:00:00Z", "2021-07-07T21:00:00Z")
    event_calender.create_user("B", "2021-07-07T9:00:00Z", "2021-07-07T21:00:00Z")
    event_calender.create_user("C", "2021-07-07T9:00:00Z", "2021-07-07T21:00:00Z")

    event_calender.create_team("T1", ["A", "B"])
    event_calender.create_event("E1", "2021-07-07T13:00:00Z", "2021-07-07T15:00:00Z",
                                ["C"], ["T1"], 1)

    event_calender.print_user("A")
    event_calender.print_user("B")
    event_calender.print_user("C")

    event_calender.create_event("E2", "2021-07-07T14:00:00Z", "2021-07-07T17:00:00Z",
                               ["C"], ["T1"], 1);

    event_calender.print_user("A")
    event_calender.print_user("B")
    event_calender.print_user("C")
