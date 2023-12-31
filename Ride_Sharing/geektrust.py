
import sys

from driver import Driver
from rider import Rider
from ride_sharing  import RideSharing


def main():

	file_path = sys.argv[1]
	fs = open(file_path, 'r')
	ride_sharing = RideSharing()

	for query in fs:

		sp_str = query.split(" ")
		
		if sp_str[0] == "ADD_DRIVER":
			driver_obj = Driver(sp_str[1].strip(), int(sp_str[2].strip()), int(sp_str[3].strip()))
			ride_sharing.add_driver(driver_obj)

		elif sp_str[0] == "ADD_RIDER":
			rider_obj = Rider(sp_str[1].strip(), int(sp_str[2].strip()), int(sp_str[3].strip()))
			ride_sharing.add_rider(rider_obj)

		elif sp_str[0] == "MATCH":
			ride_sharing.match_driver(sp_str[1].strip())

		elif sp_str[0] == "START_RIDE":
			ride_sharing.start_ride(sp_str[1].strip(), int(sp_str[2].strip()), sp_str[3].strip())

		elif sp_str[0] == "STOP_RIDE":
			ride_sharing.stop_ride(sp_str[1].strip(), int(sp_str[2].strip()), int(sp_str[3].strip()), int(sp_str[4].strip()))

		elif sp_str[0] == "BILL":
			ride_sharing.get_fair(sp_str[1].strip())


if __name__ == "__main__":

	main()