

1. Clarify And Gather Functional Requirements:


    1. Create User with working hour
    2. Assigned User in team : create Team.
        user can be part of only one team.

    3. User Can Create Event for particular time slot:
        can choose team with minimum representative.
        can choose single user

        check for team representative availability as well as single user availability.

    4. Get Event for particular User for given time range.

    5. Get available time slot for given users, or given teams as well as users and teams for
       current day


    store all data in memory rathar than in database.


    user_hash_map = {"name": {"name", "sex":"", "role": "", "team":None}}
    team_hash_map = {"team_name": set()}
    user_working_hours = {"name": time, "name": "time"}

    events = {"8AM_10PM": {"name", "users": set(), "teams": set()}}


    create user = {"A": {"name":"A",
                        "age": 29,
                        "sex": "M",
                        "start_hour": "8AM",
                        "end_hour": "10PM",
                        "team": "team1",
                        "events": {
                        "8AM_8:30AM": "event1"
                        }}}

    create Team ={"team1": set("A", "B")}


    create event -- 8am - 8:30, users = A, team1= team1, 2







