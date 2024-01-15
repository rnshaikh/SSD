
from heapq import heappush, heappop

from src.utils import push_driver


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

		push_driver(self.match_drivers, temp)
		return temp 


	def get_match_driver(self, n):
		
		import conf

		if len(self.match_drivers) < n:
			return conf.NEGATIVE_INIT

		temp = []
		dr = None
		while n > conf.ZERO_INIT:
			driver = heappop(self.match_drivers)
			dr = driver
			temp.append(driver)
			n = n-conf.ONE_INIT

		push_driver(self.match_drivers, temp)

		if dr:
			return dr[conf.ONE_INIT] 
		return conf.NEGATIVE_INIT


