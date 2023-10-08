

class Team:

    def __init__(self, name):

        self.name = name
        self.participant = set()

    def get_name(self):
        return self.name

    def get_participants(self):
        return self.participant

    def add_member(self, user):
        self.participant.add(user)
        user.team = self
