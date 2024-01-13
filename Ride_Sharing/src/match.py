import math
import conf

from heapq import heappush, heappop
from src.utils import my_round



def calculate_ecd(start_x_co, start_y_co, end_x_co, end_y_co):
	
	ans = (end_x_co - start_x_co) ** conf.TWO + (end_y_co - start_y_co) ** conf.TWO
	ans = math.sqrt(ans)
	ans = my_round(ans, conf.TWO)
	ans = (ans*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
	return ans


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

