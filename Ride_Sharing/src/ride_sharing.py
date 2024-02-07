import time

from src.rider import Rider
from src.driver import Driver
from src.ride import Ride
from src.fair import ECDFair
from src.validator import (validate_start_ride, validate_rider, validate_match_driver_id,
						   validate_match_driver, validate_ride_id_already_exist, check_match_driver,
						   validate_rider_already_exist, check_ride_id_is_not_exist, 
						   check_ride_is_completed, check_ride_exists, check_ride_completed)
from src.utils import match_driver


class RideSharing:

	def __init__(self):

		self.rides = {}
		self.riders = {}
		self.drivers = {}
		self.fair_obj = ECDFair()

	def add_rider(self, rider):

		try:
			validate_rider_already_exist(rider, self.riders)
			self.riders[rider.get_id()] = rider

		except Exception as e:
			print(e)

	def add_driver(self, driver):

		if driver.id in self.drivers:
			print("DRIVER_ALREADY_EXIST")
		self.drivers[driver.get_id()] = driver

	def match_driver(self, rider_id):

		try:

			rider = self.riders.get(rider_id, None)
			validate_rider(rider)
			match_drivers = match_driver(rider, self.drivers)
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
			rider_location = rider.get_location()
			ride_obj = Ride(ride_id, rider, match_driver, rider_location[0], rider_location[1])
			match_driver.update_available()

			self.rides[ride_id] = ride_obj
			print("RIDE_STARTED {ride_id}".format(ride_id = ride_id))

		except Exception as e:
			print(e)


	def stop_ride(self, ride_id, x_co, y_co, time_taken):

		try:
			ride = self.rides.get(ride_id, None)
			check_ride_exists(ride)
			check_ride_completed(ride)
			ride.stop_ride(x_co, y_co, time_taken)
			ride.driver.update_available()
			print("RIDE_STOPPED {ride_id}".format(ride_id=ride_id))

		except Exception as e:
			print(e)


	def get_fair(self, ride_id):

		try:
			check_ride_id_is_not_exist(ride_id, self.rides)
			ride = self.rides[ride_id]
			check_ride_is_completed(ride)
			fair = self.fair_obj.calculate(ride)
			ride.add_fair(fair)
			print("BILL {ride_id} {driver_id} {fair}".format(ride_id=ride_id, driver_id=ride.driver.get_id(),
															 fair="{:.2f}".format(ride.fair)))
		except Exception as e:
			print(e)
