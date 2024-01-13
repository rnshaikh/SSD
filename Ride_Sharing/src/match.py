import math
import conf

from heapq import heappush, heappop
from src.utils import my_round, calculate_ecd


class Match:

	def match_rider(self, rider):
		pass


class EcMatch(Match):

	def match_driver(self, rider, drivers):

		match_drivers = []

		for driver in drivers:
			if drivers[driver].is_available():
				ans = calculate_ecd(rider.x_co,rider.y_co, drivers[driver].x_co, drivers[driver].y_co)
				if ans <= conf.MAX_DRIVER_SHOW:
					heappush(match_drivers, (ans, driver))
		return match_drivers

