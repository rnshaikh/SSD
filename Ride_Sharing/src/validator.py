import conf


def validate_rider(rider):

	if not rider:
		print("INVALID_RIDER")
		return

def validate_start_ride(rider):

	if not rider.match_done:
		print("MATCH_IS_NOT_HAPPEND")
		return

def validate_match_driver_id(match_driver_id):

	if match_driver_id == conf.NEGATIVE_INIT:
		print("INVALID_RIDE")
		return

def validate_match_driver(match_driver):

	if not match_driver or not match_driver.is_available():
			print("INVALID_RIDE")
			return

def validate_ride_id_already_exist(ride_id, rides):

	if ride_id in rides:
		print("INVALID RIDE")
		return 

def check_match_driver(match_drivers):

	if len(match_drivers):
		ans = ""
		for driver in match_drivers:
			ans += driver[1]
			ans += " "
		print("DRIVERS_MATCHED  {ans}".format(ans=ans))
	else:
		print("NO_DRIVERS_AVAILABLE")
		return
