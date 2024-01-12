
from heapq import heappush, heappop

ZERO_INIT = 0

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

	def get_match_drivers(self):

		temp = []

		while self.match_drivers:
			temp.append(heappop(self.match_drivers))

		for temp_driver in temp:
			heappush(self.match_drivers, temp_driver)
		return temp 


	def get_match_driver(self, n):
		
		if len(self.match_drivers) < n:
			return -1

		temp = []
		dr = None
		while n > ZERO_INIT:
			driver = heappop(self.match_drivers)
			dr = driver
			temp.append(driver)
			n = n-1

		for temp_driver in temp:
			heappush(self.match_drivers, temp_driver)

		if dr:
			return dr[1] 
		else:
			return -1


