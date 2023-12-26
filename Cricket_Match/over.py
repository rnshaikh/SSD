
from ball import Ball


class Over:

	def __init__(self):
		self.balls = []
		self.total_ball_bowled = 0
		
		self.total_no_ball = 0
		self.total_wide_ball = 0
		self.total_wickets = 0

	def add_ball(self, b):

		b_obj = Ball()

		if b not in ['Wd', 'W', 'N']:
			b_obj.add_run(b)
		else:
			if b == "Wd":
				b_obj.add_wide(b)
			elif b == "W":
				b_obj.add_wicket(b)
			elif b == "N":
				b_obj.add_no(b)
			else:
				print("Invalid entity for ball")
				return

		self.ball.add(b_obj)

