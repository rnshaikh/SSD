

class Consitituency:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_votes(self, votes):
        self.votes += votes

    def get_votes(self, votes):
        return self.votes
