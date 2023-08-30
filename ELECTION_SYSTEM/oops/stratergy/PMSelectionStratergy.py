import heapq
from stratery import ConstituencyWinnerStratergy, PartyPMCandidate


class PMSelectionStratergy:

    def __init__(self, country):
        self.country = country

    def find_pm(self):

        cws = ConstituencyWinnerStratergy(self.country)
        PartyPMCandidate(cws, self.country)

        parties = self.country.parties
        heap = []

        for party in parties:
            heapq.heappush(heap, (-party.winning_count, -party.PMCVotePerc, party.name))

        winning_party = heapq.heappop(heap)
        winner = parties[winning_party[2]]

        return winner.PMCandiate
