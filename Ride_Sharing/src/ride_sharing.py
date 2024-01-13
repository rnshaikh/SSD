import time

from src.rider import Rider
from src.driver import Driver
from src.ride import Ride, Status
from src.match import EcMatch
from src.fair import ECDFair
from src.validator import (validate_start_ride, validate_rider, validate_match_driver_id,
						   validate_match_driver, validate_ride_id_already_exist, check_match_driver,
						   validate_rider_already_exist)


class RideSharing:

	def __init__(self):

		self.rides = {}
		self.riders = {}
		self.drivers = {}
		self.EcMatch = EcMatch()

	def add_rider(self, rider):

		try:
			validate_rider_already_exist(rider, self.riders)
			self.riders[rider.id] = rider

		except Exception as e:
			print(e)

	def add_driver(self, driver):

		if driver.id in self.drivers:
			print("DRIVER_ALREADY_EXIST")
		self.drivers[driver.id] = driver

	def match_driver(self, rider_id):

		try:

			rider = self.riders.get(rider_id, None)
			validate_rider(rider)
			match_drivers = self.EcMatch.match_driver(rider, self.drivers)
			rider.add_match_driver(match_drivers)
			match_drivers = rider.get_match_drivers()
			check_match_driver(match_drivers)

		except Exception as e:
			print(e)


	def start_ride(self, ride_id, n, rider_id):
		
		try:	
			validate_ride_id_already_exist(ride_id, self.rides)
			rider = self.riders.get(rider_id, None)
			validate_rider(rider)
			validate_start_ride(rider)
			match_driver_id = rider.get_match_driver(n)
			validate_match_driver_id(match_driver_id)
			match_driver = self.drivers.get(match_driver_id, None)
			validate_match_driver(match_driver)	
			ride_obj = Ride(ride_id, rider, match_driver, rider.x_co, rider.y_co)
			match_driver.update_available()

			self.rides[ride_id] = ride_obj
			print("RIDE_STARTED {ride_id}".format(ride_id = ride_id))

		except Exception as e:
			print(e)


	def stop_ride(self, ride_id, x_co, y_co, time_taken):


		ride = self.rides.get(ride_id, None)

		if not ride:
			print("INVALID_RIDE")
			return

		if ride.status == Status.COMPLETED.value:
			print("INVALID_RIDE")
			return

		ride.stop_ride(x_co, y_co, time_taken)
		ride.driver.update_available()
		print("RIDE_STOPPED {ride_id}".format(ride_id=ride_id))


	def get_fair(self, ride_id):

		if ride_id not in self.rides:
			print("INVALID_RIDE")
			return

		ride = self.rides[ride_id]

		if not ride.is_ride_completed():
			print("RIDE_NOT_COMPLETED")
			return 

		fair_obj = ECDFair()
		fair = fair_obj.calculate(ride)
		ride.add_fair(fair)

		print("BILL {ride_id} {driver_id} {fair}".format(ride_id=ride_id, driver_id=ride.driver.id,
														 fair="{:.2f}".format(ride.fair)))

