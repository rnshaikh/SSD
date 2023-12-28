
from over import Over


class Score:

	def __init__(self):
		curr_player = []
		total_overs = 0
		total_wickets = 0
		curr_over = 0.0
		total_wide = 0
		total_no = 0
		total_wickets_fall = 0

	def add_curr_player(self, player):

		if len(curr_player) == 2:
			print("can't bat more than 2 player")

		curr_player.append(player)

	def remove_curr_player(self, player):

		try:
			if self.total_wickets_fall == self.total_wickets:
				print("Team already all out.")
				return
			arr.remove(player)
			self.total_wickets_fall += 1
		except Exception:
			print("player is not playing currently")


	def add_total_overs(self, total_overs):
		self.total_overs = total_overs

	





