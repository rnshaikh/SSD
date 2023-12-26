

class Ball:

	def __init__(self):
		run = 0
		wide = False
		no = False
		wicket = False
	
	def add_run(self, run):

		if run not in [1, 2, 3, 4, 6]:
			print("Invalid Score")
			return
		self.run += 1

	def add_wide(self):
		self.wide = True

	def add_wicket(self):
		self.wicket = True

	def add_no(self):
		self.no = True


