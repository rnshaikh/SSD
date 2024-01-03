from enum import Enum


class Status(Enum):

	STARTED = "STARTED"
	COMPLETED = "COMPLETED"



class Ride:

	def __init__(self, ride_id, rider, driver, start_x_co, start_y_co):

		self.ride_id = ride_id
		self.rider = rider
		self.driver = driver
		self.start_x_co = start_x_co
		self.start_y_co = start_y_co
		self.dest_x_co = None
		self.dest_x_co = None
		self.time_taken = 0
		self.status = Status.STARTED.value


	def stop_ride(self, dest_x_co, dest_y_co, time_taken):

		self.dest_x_co = dest_x_co
		self.dest_y_co = dest_y_co
		self.time_taken = time_taken
		self.status = Status.COMPLETED.value

