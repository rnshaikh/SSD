
class Driver:

	def __init__(self, id, x_co, y_co):
		self.id = id
		self.x_co = x_co
		self.y_co = y_co
		self.available = True

	def is_available(self):

		return self.available 

	def update_available(self):

		self.available = not self.available

	def update_location(self, x_co, y_co):
		self.x_co = x_co
		self.y_co = y_co

