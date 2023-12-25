

class Team:

	def __init__(self, name, no_of_player):

		self.name = name
		self.no_of_player = no_of_player
		self.players = []


	def add_player(self, player):

		if len(self.players) > no_of_player:
			print("Can't add more player")
			return
		self.players.append(player)
	