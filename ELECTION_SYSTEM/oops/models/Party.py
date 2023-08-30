

class Party:

    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def add_votes(self, votes):
        self.votes += votes

    def get_name(self):
        return self.name
