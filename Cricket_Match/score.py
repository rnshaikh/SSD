

class Score:

	def __init__(self):
		curr_player = []
		total_overs = 0
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
			arr.remove(player)
		except Exception:
			print("player is not playing currently")

	def add_total_overs(self, total_overs):
		self.total_overs = total_overs


	def update_curr_over(self):

		if self.curr_overs > total_overs:
			return print("Over Finished")

		frac = self.curr_overs - int(self.curr_overs)
		if frac == 0.5:
			self.curr_overs = int(self.curr_overs) + 1.0


