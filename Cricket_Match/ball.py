

class Ball:

	def __init__(self):
		self.run = 0
		self.wide = False
		self.no = False
		self.wicket = False
	
	def add_run(self, run):

		if run not in [1, 2, 3, 4, 6]:
			print("Invalid Score")
			return
		self.run += run

	def add_wide(self):
		self.wide = True

	def add_wicket(self):
		self.wicket = True

	def add_no(self):
		self.no = True
