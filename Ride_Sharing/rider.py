

class Rider:

	def __init__(self, id, x_co, y_co):
		self.id = id
		self.x_co = x_co
		self.y_co = y_co
		self.match_drivers = []
		self.match_done = False


	def add_match_driver(self, match_drivers):
		self.match_drivers = match_drivers
		self.match_done = True

	def get_match_driver(self):
		return self.match_drivers

