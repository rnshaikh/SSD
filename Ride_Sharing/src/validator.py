import conf


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
		
