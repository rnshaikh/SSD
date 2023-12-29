

class Player:

	def __init__(self, name):
		self.name = name
		self.score = 0
		self.ball_faced = 0
		self.no_fours = 0
		self.no_sixes = 0
		self.no_ones = 0
		self.no_twos = 0
		self.no_threes= 0
		

	def add_score(self, score):

		if score not in [1, 2, 3, 4,6]:
			print("Invalid Score")
			return

		self.score += score
		self.ball_faced += 1

		if score == 1:
			self.no_ones+=1
		elif score == 2:
			self.no_twos+=1
		elif score == 3:
			self.no_threes+=1
		elif score == 4:
			self.no_fours+=1
		else:
			self.no_sixes+=1