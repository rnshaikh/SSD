import conf
from src.ride import Status


def validate_rider(rider):

	if not rider:
		raise Exception("INVALID_RIDER")
		

def validate_start_ride(rider):

	if not rider.match_done:
		raise Exception("MATCH_IS_NOT_HAPPEND")
		

def validate_match_driver_id(match_driver_id):

	if match_driver_id == conf.NEGATIVE_INIT:
		raise Exception("INVALID_RIDE")
		

def validate_match_driver(match_driver):

	if not match_driver or not match_driver.is_available():
		raise Exception("INVALID_RIDE")
			

def validate_ride_id_already_exist(ride_id, rides):

	if ride_id in rides:
		raise Exception("INVALID_RIDE")
		 

def check_match_driver(match_drivers):

	if len(match_drivers):
		ans = ""
		for driver in match_drivers:
			ans += driver[1]
			ans += " "
		raise Exception("DRIVERS_MATCHED  {ans}".format(ans=ans))
	else:
		raise Exception("NO_DRIVERS_AVAILABLE")
		

def validate_rider_already_exist(rider, riders):

	if rider.id in riders:
		raise Exception("RIDER_ALREADY_EXIST")
		

def check_ride_id_is_not_exist(ride_id, rides):

	if ride_id not in rides:
		raise Exception("INVALID_RIDE")

def check_ride_is_completed(ride):

	if not ride.is_ride_completed():
		raise Exception("RIDE_NOT_COMPLETED")

def check_ride_exists(ride):

	if not ride:
		raise Exception("INVALID_RIDE")

def check_ride_completed(ride):

	if ride.status == Status.COMPLETED.value:
		raise Exception("INVALID_RIDE")
