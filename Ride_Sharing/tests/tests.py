import io
import sys
import unittest
import conf

from geektrust import main


class TestRideSharing(unittest.TestCase):


	def test_ride_sharing1(self):
		sys.argv[conf.ONE_INIT] = 'sample_input\\input2.txt'
		capture_output = io.StringIO()
		sys.stdout = capture_output
		out = main()
		sys.stdout = sys.__stdout__
		check  = capture_output.getvalue().strip()
		out_st = capture_output.getvalue().strip()

		self.assertEqual(out_st, check)


	def test_ride_sharing2(self):
		sys.argv[conf.ONE_INIT] = 'sample_input\\input1.txt'
		capture_output = io.StringIO()
		sys.stdout = capture_output
		out = main()
		sys.stdout = sys.__stdout__
		check  = capture_output.getvalue().strip()
		out_st = capture_output.getvalue().strip()

		self.assertEqual(out_st, check)


	def test_invalid_ride_sharing2(self):
		sys.argv[conf.ONE_INIT] = 'sample_input\\input3.txt'
		capture_output = io.StringIO()
		sys.stdout = capture_output
		out = main()
		sys.stdout = sys.__stdout__
		check  = capture_output.getvalue().strip()
		out_st = capture_output.getvalue().strip()
		self.assertEqual(out_st, check)
		