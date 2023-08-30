
class ConstituencyParty:

    def __init__(self):
        self.constituency =  None
        self.party = None
        self.candidate = None

    def add_constituency_party(self, constituency, party, candidate):

        self.constituency = constituency
        self.party = party

    def add_candidate(self, candidate):
        self.candidate = candidate


