import json
import heapq


class InputClass:

    def __init__(self, file_path):
        self.file_path = file_path
        self.objects = None

    def process_input(self):

        with open(self.file_path, 'r') as f:
            self.objects = json.load(f)
        self.setup_data()

    def setup_data(self):

        cons = {}
        party_wise_cons = {}
        total_country_votes = 0
        candidates_cons = []
        party_wise_share = []

        for obj in self.objects:
            if obj['constituency'] not in cons:
                cons[obj['constituency']] = {}
                cons[obj['constituency']]['cons'] = []
            heapq.heappush(cons[obj['constituency']]['cons'], (-obj['votes'], obj['party'], obj['name']))
            total_country_votes += obj['votes']

        for key in cons:
            total_votes = 0
            for i in cons[key]['cons']:
                total_votes += (-i[0])
                heapq.heappush(candidates_cons, (i[0], i[1], i[2], key))
            cons[key]['total_votes'] = total_votes
            if cons[key]['cons'][0][0] != cons[key]['cons'][1][0]:
                cons[key]['winner'] = cons[key]['cons'][0]
                cons[key]['winner_percentage'] = (-cons[key]['cons'][0][0] / cons[key]['total_votes']) * 100
            else:
                cons[key]['winner'] = None
                cons[key]['winner_percentage'] = None

            if cons[key]['winner']:
                if cons[key]['winner'][1] not in party_wise_cons:
                    party_wise_cons[cons[key]['winner'][1]] = {}

                if 'count' not in party_wise_cons[cons[key]['winner'][1]]:
                    party_wise_cons[cons[key]['winner'][1]]['count'] = 0

                if 'cons' not in party_wise_cons[cons[key]['winner'][1]]:
                    party_wise_cons[cons[key]['winner'][1]]['cons'] = []

                if 'total_votes' not in party_wise_cons[cons[key]['winner'][1]]:
                    party_wise_cons[cons[key]['winner'][1]]['total_votes'] = 0

                party_wise_cons[cons[key]['winner'][1]]['count'] += 1
                heapq.heappush(party_wise_cons[cons[key]['winner'][1]]['cons'], cons[key]['winner'])
                party_wise_cons[cons[key]['winner'][1]]['total_votes'] += (-cons[key]['winner'][0])
                party_wise_cons[cons[key]['winner'][1]]['vote_percentage'] = (party_wise_cons[cons[key]['winner'][1]]['total_votes'] / total_country_votes) * 100

        for key in party_wise_cons:
            heapq.heappush(party_wise_share, (-party_wise_cons[key]['vote_percentage'], key))


        print("constituency", cons)
        print("party wise cons", party_wise_cons)
        print("candidates_cons", candidates_cons)
        print("party_wise_share", party_wise_share)
        print("total country votes", total_country_votes)
        return cons, party_wise_cons, candidates_cons, party_wise_share, total_country_votes
