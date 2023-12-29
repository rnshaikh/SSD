
from ball import Ball


class Over:

	def __init__(self):
		self.balls = []
		self.total_ball_bowled = 0
		
		self.total_run = 0
		self.total_no_ball = 0
		self.total_wide_ball = 0
		self.total_wickets = 0
		self.player = None


	def add_player(self, player):
		self.player = player

	def add_ball(self, b):

		b_obj = Ball()

		if b not in ['Wd', 'W', 'N']:
			b_obj.add_run(int(b))
			self.total_run += int(b)
		else:
			if b == "Wd":
				b_obj.add_wide()
				self.total_wide_ball += 1
			elif b == "W":
				b_obj.add_wicket()
				self.total_wickets += 1

			elif b == "N":
				b_obj.add_no()
				self.total_no_ball += 1

			else:
				print("Invalid entity for ball")
				return

		self.balls.append(b_obj)
		self.total_ball_bowled += 1


