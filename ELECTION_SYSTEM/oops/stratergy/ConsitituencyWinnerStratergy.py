from stratery import PartyPMCandidate

class ConstituencyWinnerStratergy:


    def __init__(self):
        self.map = {}

    def calculatewinners(self, country):

        consitituencies = country.constituencies
        for constituency in consitituencies:
            cname = constituency.name
            max_votes = 0
            max_candidate = None
            max_party = None

            for cp in country.constituencies_party:
                const, party = cp.split("-")
                if const == cname:
                    cps = country.constituencies_party[cp]
                    c_votes = cps.candidate.get_votes()
                    if c_votes > max_votes:
                        max_votes = c_votes
                        max_candidate = cps.candidate
                        max_party = country.parties[party]

            max_party.winning_count += 1
            self.map[cname] = (max_votes, max_candidate, max_party)

        PartyPMCandidate(self)


