import math

from abc import ABC

from src.match import calculate_ecd


class BaseFair(ABC):

	def calculate(self):
		pass



class ECDFair(BaseFair):

	def __init__(self):
		self.base = 50
		self.per_km = 6.5
		self.per_minute = 2
		self.service_tax = 0.2

	def calculate(self, ride):

		dist = calculate_ecd(ride.start_x_co, ride.start_y_co,
							 ride.dest_x_co, ride.dest_y_co)

		fair = self.base + (dist * self.per_km) + (ride.time_taken * 2)
		service_tax = self.service_tax * fair 
		fair = fair + service_tax
		fair = math.ceil(fair*100)/100
		return fair
		
