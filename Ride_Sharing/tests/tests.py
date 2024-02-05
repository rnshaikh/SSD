import io
import sys
import unittest
import conf

from geektrust import main
from src.driver import Driver
from src.rider import Rider
from src.ride import Ride
from src.ride_sharing import RideSharing

class TestRideSharing(unittest.TestCase):

	
	def test_driver_available(self):
		driver_obj =  Driver('D1',1,1)
		self.assertEqual(driver_obj.is_available(), True)

	def test_driver_not_available(self):
		driver_obj =  Driver('D1',1,1)
		driver_obj.update_available()
		self.assertEqual(driver_obj.is_available(), False)


	def test_fair(self):
		ride_sharing_obj = RideSharing()
		capture_output = io.StringIO()
		sys.stdout = capture_output
		driver_obj = Driver('D1', 1, 1)
		rider_obj = Rider('R1',0, 0)
		ride_sharing_obj.add_rider(rider_obj)
		ride_sharing_obj.add_driver(driver_obj)
		ride_sharing_obj.match_driver('R1')
		ride_sharing_obj.start_ride("RIDE-001", 1, "R1")
		sys.stdout = sys.__stdout__
		capture_output = io.StringIO()
		sys.stdout = capture_output
		ride_sharing_obj.stop_ride("RIDE-001",4, 5, 32)
		sys.stdout = sys.__stdout__
		capture_output = io.StringIO()
		sys.stdout = capture_output
		ride_sharing_obj.get_fair("RIDE-001")
		sys.stdout = sys.__stdout__
		ans = capture_output.getvalue().strip()
		self.assertEqual(ans, 'BILL RIDE-001 D1 186.72')


