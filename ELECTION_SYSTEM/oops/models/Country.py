from models import Party, Constituency, ConstituencyParty


class Country:

    def __init__(self, name):

        self.name = name
        self.parties = {}
        self.constituencies = {}
        self.constituencies_party = {}
        self.candidateCP = {}
        self.pm_stratergy = None
        self.votes = 0

    def add_party(self, party):
        name = party.get_name()
        if name in self.parties:
            raise Exception("Party already is present")
        self.parties[name] = party

    def add_constituencies(self, constituency):
        name = constituency.get_name()
        if name in self.constituencies:
            raise Exception("Constituency already present")
        self.constituencies[name] = constituency

    def add_pm_stratergy(self, pm_stratergy):
        self.pm_stratergy = pm_stratergy

    def add_constituencies_party(self, constituency, party):
        key = constituency.name + "-" + party.name
        if key in self.constituencies_party:
            raise Exception("already Present")

        cps = ConstituencyParty(constituency, party, candidate)
        self.constituencies_party[key] = cps

    def add_candidate(self, constituency, party, candidate):

        key = constituency.name + "-" + party.name
        if key in self.constituencies_party:
            cps = self.constituencies_party[key]
            cps.add_candidate(candidate)
        else:
            key = constituency.name + "-" + party.name
            cps = ConstituencyParty(constituency, party, candidate)
            self.constituencies_party[key] = cps

        constituency.add_votes(candidate.votes)
        party.add_votes(candidate.votes)
        self.add_votes(candidate.votes)
        self.candidateCP[candidate.get_name()] = cps

    def add_votes(self, votes):
        self.votes += votes

    def find_pm(self):
        self.pm_stratergy.find_pm()

    def get_party_wise_vote_share(self, constituency):

        name = constituency.get_name()
        total_votes = constituency.get_votes()

        for cpk in self.constituencies_party:
            constituency, party = cpk.split("-")
            if constituency == name:
                party_obj = self.parties[party]
                print("party: %s, votes_share: %s" %(party_obj.get_name(), party_obj.get_votes()* 100/total_votes))

    def get_candidate_vote_share(self, candidate):

        name = candidate.get_name()
        cps = self.candidateCP[name]
        constituency = cps.constituency

        total_votes = constituency.get_votes()

        return candidate.get_votes() * 100 / total_votes










