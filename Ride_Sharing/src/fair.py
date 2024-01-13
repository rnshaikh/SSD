import math
import conf

from abc import ABC, abstractmethod

from src.match import calculate_ecd
from src.utils import my_round


class BaseFair(ABC):

	@abstractmethod
	def calculate(self):
		pass

	@abstractmethod
	def calculate_distance_fair(self):
		pass

	@abstractmethod
	def calculate_time_taken_fair(self):
		pass

	@abstractmethod
	def calculate_service_tax(self):
		pass


class ECDFair(BaseFair):

	def __init__(self):
		self.base = conf.BASE_PRICE
		self.per_km = conf.PER_KM
		self.per_minute = conf.PER_MINUTE
		self.service_tax = conf.SERVICE_TAX


	def calculate_distance_fair(self, dist):

		result = dist * self.per_km
		return result


	def calculate_time_taken_fair(self, ride):

		time_fair = (ride.time_taken * self.per_minute)
		return time_fair


	def calculate_service_tax(self, fair):

		service_tax = (self.service_tax * fair)
		#print("service", service_tax)
		service_tax = my_round(service_tax, conf.TWO) 
		return service_tax


	def calculate(self, ride):

		dist = calculate_ecd(ride.start_x_co, ride.start_y_co,
							 ride.dest_x_co, ride.dest_y_co)

		distance_fair = self.calculate_distance_fair(dist)
		time_taken_fair = self.calculate_time_taken_fair(ride)
		fair = self.base + distance_fair + time_taken_fair
		service_tax = self.calculate_service_tax(fair)
		fair = my_round(fair, conf.TWO)
		fair = fair + service_tax
		fair = my_round(fair, conf.TWO)
		fair = (fair*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
		return fair
		
