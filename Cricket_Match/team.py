

class Team:

	def __init__(self, name):

		self.name = name
		self.no_of_player = 0
		self.players = []
		self.next_batsman = 0
		self.total_wickets = 0
		self.total_wicket_fallen = 0
		self.total_score = 0
		self.is_batting = False
		self.current_batsman = None
		self.strike_batsman = None

	def add_total_no_player(self, no):
		self.no_of_player = no
		self.total_wickets = no

	def add_player(self, player):

		if len(self.players) > self.no_of_player:
			print("Can't add more player")
			return
		self.players.append(player)


	def initialized_batsman(self):

		self.strike_batsman = self.players[self.next_batsman]
		self.next_batsman+=1
		self.current_batsman = self.players[self.next_batsman]
		
	
	def change_batting(self):
		self.is_batting = not self.is_batting

	def update_wicket_fallen(self):

		self.total_wicket_fallen += 1

	def is_batsman_available(self):

		print("Is total total_wicket_fallen", self.total_wicket_fallen, self.no_of_player)

		return self.total_wicket_fallen < self.no_of_player

	def update_score(self, score):
		if score not in [1, 2, 3, 4,6]:
			print("Invalid Score")
			return
		self.total_score += score

	def update_batting(self):
		self.is_batting = not self.is_batting

	def change_strike_after_over(self):
		self.current_batsman, self.strike_batsman = self.strike_batsman, self.current_batsman

	def change_strike_after_wicket_fallen(self, is_strike):

		if is_strike:
			self.strike_batsman = self.players[self.next_batsman]
			self.next_batsman += 1
		else:
			self.current_batsman = self.players[self.next_batsman]
			self.next_batsman += 1

