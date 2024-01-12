import math
import conf

from abc import ABC

from src.match import calculate_ecd


class BaseFair(ABC):

	def calculate(self):
		pass



class ECDFair(BaseFair):

	def __init__(self):
		self.base = conf.BASE_PRICE
		self.per_km = conf.PER_KM
		self.per_minute = conf.PER_MINUTE
		self.service_tax = conf.SERVICE_TAX


	def calculate_distance_fair(self, dist):

		decimal_part = dist % 1
		decimal_part = math.ceil(decimal_part*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
		int_part = int(dist)

		result = int_part * self.per_km
		result += (decimal_part*self.per_km)
		print("dist result ", result)
		return result


	def calculate_time_taken_fair(self, ride):

		time_fair = (ride.time_taken * self.per_minute)
		print("tim", time_fair)
		return time_fair


	def calculate_service_tax(self, fair):

		service_tax = (self.service_tax * fair)
		print("service", service_tax)
		return service_tax


	def calculate(self, ride):

		dist = calculate_ecd(ride.start_x_co, ride.start_y_co,
							 ride.dest_x_co, ride.dest_y_co)

		print("dist", dist)

		distance_fair = self.calculate_distance_fair(dist)
		print("dist fair", distance_fair)

		time_taken_fair = self.calculate_time_taken_fair(ride)
		print("time taken fair", time_taken_fair)

		fair = self.base + distance_fair + time_taken_fair
		#fair = math.ceil(fair*conf.PERC_DIVISOR)/conf.PERC_DIVISOR

		print("result before service", fair)

		service_tax = self.calculate_service_tax(fair)
		fair = fair + service_tax
		fair = math.ceil(fair*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
		return fair
		
