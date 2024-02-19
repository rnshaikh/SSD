import io
import sys
import unittest
import conf

from src.station import Station
from src.metrocard import MetroCard
from src.program_driver import ProgramDriver


class MetroTest(unittest.TestCase):

	def setUp(cls):
		cls.driver_obj = ProgramDriver()
		cls.driver_obj.add_station()
		cls.driver_obj.add_metrocard('MC1', 600)

	def test_add_metro_card(self):
		obj = self.driver_obj.metro_cards['MC1']
		self.assertEqual(self.driver_obj.metro_cards['MC1'], obj)

	def test_check_in(self):
		self.driver_obj.check_in('MC1','ADULT', 'CENTRAL')
		self.driver_obj.check_in('MC1','ADULT', 'AIRPORT')
		self.assertEqual(self.driver_obj.metro_cards['MC1'].get_amount(), 300)

	def test_check_print_summary(self):
		self.driver_obj.check_in('MC1','ADULT', 'CENTRAL')
		self.driver_obj.check_in('MC1','ADULT', 'AIRPORT')
		capture_output = io.StringIO()
		sys.stdout = capture_output
		self.driver_obj.print_summary()
		sys.stdout = sys.__stdout__
		ans = capture_output.getvalue().strip()
		self.assertTrue("CENTRAL 200 0\n" in ans)
		self.assertTrue("AIRPORT 100 100\n" in ans)


