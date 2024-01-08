import math
from heapq import heappush, heappop



def calculate_ecd(start_x_co, start_y_co, end_x_co, end_y_co):

	ans = (end_x_co - start_x_co) ** 2 + (end_y_co - start_y_co) ** 2 
	ans = math.sqrt(ans)
	ans = math.ceil(ans*100)/100
	return ans


class Match:

	def match_rider(self, rider):
		pass


class EcMatch(Match):

	def match_driver(self, rider, drivers):

		match_drivers = []

		for driver in drivers:
			ans = calculate_ecd(rider.x_co,rider.y_co, drivers[driver].x_co, drivers[driver].y_co)
			if ans <= 5:
				heappush(match_drivers, (ans, driver))
		return match_drivers

