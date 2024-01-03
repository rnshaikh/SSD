import time
from rider import Rider
from driver import Driver

from ride_ import Ride

from match import EcMatch
from fair import Fair



class Ride:

	def __init__(self):

		self.rides = {}
		self.riders = {}
		self.drivers = {}
		self.EcMatch = EcMatch()

	def add_rider(self, rider):
		self.riders[rider.id] = rider

	def add_driver(self, driver):
		self.drivers[driver.id] = driver

	def match_driver(self, rider_id):

		rider = self.riders.get(rider_id, None)

		if not rider:
			print("Invalid Rider")
			return

		match_drivers = self.EcMatch.match_driver(rider, self.drivers)
		rider.add_match_driver(match_drivers)

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
			print("Invalid Rider")

		match_drivers = rider.get_match_driver()

		if len(match_drivers) < n:
			print("Driver Not Available")


		if ride_id in self.rides:
			print("INVALID_RIDE")

		dis, match_driver = match_drivers[n-1]

		ride_obj = Ride(ride_id, rider, self.drivers[match_driver], rider.x_co, rider.y_co)

		self.rides[ride_id] = ride_obj
		print("RIDE_STARTED {ride_id}".format(ride_id = ride_id))


	def stop_ride(self, ride_id, x_co, y_co, time_taken):


		ride = self.rides.get(ride_id, None)
		if not ride:
			print("Invalid Ride")

		ride.stop_ride(x_co, y_co, time_taken)	
		print("RIDE STOPPED {ride_id}".format(ride_id=ride_id))


	def get_fair(self, ride_id):

		if ride_id not in self.rides:
			print("Invalid Ride")
			return

		ride = self.rides[ride_id]
		fair_obj = Fair()
		fair = fair_obj.calculate(ride)
		self.rides[ride_id]['fair'] = fair

		print("BILL {ride_id} {driver_id} {fair}".format(ride_id=ride_id, driver_id=ride["driver"].id,
														 fair=self.rides[ride_id]['fair']))

