class PartyPMCandidate:


    def __init__(self, cws, country):
        self.cws = cws
        self.country = country

    def calculatePartyPM(self):

        for party in self.country.parties:

            pname = party.name
            max_prec = 0
            max_candidate = None

            for winner_record in self.cws:
                votes, candidate, party = winner_record

                if party.name == pname:
                    perc = votes * 100/ party.get_votes
                    if perc > max_prec:
                        max_prec = perc
                        max_candidate = candidate

            party.PMCandidate = max_candidate
            party.PMCVotePerc = max_prec
