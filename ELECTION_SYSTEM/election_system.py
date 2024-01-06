import heapq

class ElectionSystem:

    def __init__(self, input_class):
        self.input = input_class
        self.PM = None
        self.candidates = []
        self.total_country_votes = 0
        self.winner_party = None
        self.party_wise_share = None
        self.constituency, self.party_wise_constituency, self.candidates, self.party_wise_share, self.total_country_votes = self.input.setup_data()

    def calculate_pm(self):

        hash_map = []
        for key in self.party_wise_constituency:
            heapq.heappush(hash_map, (self.party_wise_constituency[key]['count'],
                                      self.party_wise_constituency[key]['vote_percentage'],
                                      key))

        party = hash_map.pop()
        party = party[2]
        pm_candidate = self.party_wise_constituency[party]['cons'][0]
        self.PM = pm_candidate
        return pm_candidate

    def get_partywise_vote_cn(self, cn):

        con = self.constituency[cn]
        party_info = {}
        for obj in con['cons']:
            vote_share = (-obj[0]  / con['total_votes']) * 100
            party_info[obj[1]] = vote_share
        return party_info

    def get_partywise_vote_share(self):
        party_info = {}
        for key in self.party_wise_constituency:
            party_info[key] = self.party_wise_constituency[key]['vote_percentage']
        return party_info

    def get_voteshare_candidate(self, candidate):

        for i in self.candidates:
            if i[2] == candidate:
                return (-i[0]/self.constituency[i[3]]['total_votes']) * 100
        return -1

    def display_top_vote_share(self, enitity, top_count):

        ans = []

        if enitity == 'candidate':
            while top_count > 0:
                can = heapq.heappop(self.candidates)
                ans.append(can)
                top_count -= 1

            for i in ans:
                heapq.heappush(self.candidates, i)
            return ans
        else:
            while top_count > 0 and self.party_wise_share:
                can = heapq.heappop(self.party_wise_share)
                ans.append(can)
                top_count -= 1

            for i in ans:
                heapq.heappush(self.party_wise_share, i)
            return ans














