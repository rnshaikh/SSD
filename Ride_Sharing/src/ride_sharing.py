import time
from src.rider import Rider
from src.driver import Driver

from src.ride import Ride

from src.match import EcMatch
from src.fair import ECDFair



class RideSharing:

	def __init__(self):

		self.rides = {}
		self.riders = {}
		self.drivers = {}
		self.EcMatch = EcMatch()

	def add_rider(self, rider):

		if rider.id in self.riders:
			print("RIDER_ALREADY_EXIST")
			return

		self.riders[rider.id] = rider

	def add_driver(self, driver):

		if driver.id in self.drivers:
			print("DRIVER_ALREADY_EXIST")
		self.drivers[driver.id] = driver

	def match_driver(self, rider_id):

		rider = self.riders.get(rider_id, None)

		if not rider:
			print("INVALID_RIDER")
			return

		match_drivers = self.EcMatch.match_driver(rider, self.drivers)
		rider.add_match_driver(match_drivers)
		match_drivers = rider.get_match_drivers()
		
		if len(match_drivers):
			ans = ""
			for driver in match_drivers:
				ans += driver[1]
				ans += " "
			print("DRIVERS_MATCHED  {ans}".format(ans=ans))
		else:
			print("NO_DRIVERS_AVAILABLE")


	def start_ride(self, ride_id, n, rider_id):
		
		rider = self.riders.get(rider_id, None)

		if not rider:
			print("INVALID_RIDER")
			return

		if not rider.match_done:
			print("MATCH_IS_NOT_HAPPEND")

		match_driver_id = rider.get_match_driver(n)

		if match_driver_id == -1:
			print("INVALID_RIDE")
			return

		if ride_id in self.rides:
			print("INVALID RIDE")
			return 

		match_driver = self.drivers.get(match_driver_id, None)
		if not match_driver or not match_driver.is_available():
			print("INVALID_RIDE")
			return
			
		ride_obj = Ride(ride_id, rider, match_driver, rider.x_co, rider.y_co)
		match_driver.update_available()

		self.rides[ride_id] = ride_obj
		print("RIDE_STARTED {ride_id}".format(ride_id = ride_id))


	def stop_ride(self, ride_id, x_co, y_co, time_taken):


		ride = self.rides.get(ride_id, None)

		if not ride:
			print("INVALID_RIDE")
			return

		ride.stop_ride(x_co, y_co, time_taken)
		ride.driver.update_available()
		print("RIDE STOPPED {ride_id}".format(ride_id=ride_id))


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

