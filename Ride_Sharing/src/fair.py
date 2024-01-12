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

	def calculate(self, ride):

		dist = calculate_ecd(ride.start_x_co, ride.start_y_co,
							 ride.dest_x_co, ride.dest_y_co)

		fair = self.base + (dist * self.per_km) + (ride.time_taken * self.per_minute)
		service_tax = self.service_tax * fair 
		fair = fair + service_tax
		fair = math.ceil(fair*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
		return fair
		
