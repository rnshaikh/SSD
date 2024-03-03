import io
import sys
import conf
from unittest import TestCase

from src.train import Train


class TrainTestCase(TestCase):


	def setUp(cls):
		cls.boggies_a = ["TRAIN_A", "ENGINE","NDL","NDL","KRN","GHY","SLM","NJP","NGP","BLR"]
		cls.boggies_b = ["TRAIN_B", "ENGINE", "NJP", "GHY", "AGA", "PNE", "MAO","BPL", "PTA"]
		cls.train_a = Train(cls.boggies_a[0], conf.TRAIN_PATH[cls.boggies_a[0]])
		cls.train_a.add_boggey(cls.boggies_a[1:])
		cls.train_b = Train(cls.boggies_b[0], conf.TRAIN_PATH[cls.boggies_b[0]])
		cls.train_b.add_boggey(cls.boggies_b[1:])

	def test_train_arrival(self):
		
		capture_output = io.StringIO()
		sys.stdout = capture_output
		self.train_a.on_arrival(conf.MERGE_STATION)
		sys.stdout = sys.__stdout__
		ans = capture_output.getvalue().strip()
		self.assertTrue("ARRIVAL TRAIN_A ENGINE NDL NDL GHY NJP NGP" in ans)

	def test_train_merge(self):

		capture_output = io.StringIO()
		sys.stdout = capture_output
		train_obj = Train(conf.MERGE_TRAIN_NAME, conf.TRAIN_PATH[conf.MERGE_TRAIN_NAME])
		boggies = self.train_a.train + self.train_b.train
		train_obj.ordered_boggey_by_distance(boggies)
		train_obj.print_train(conf.DEPARTURE)
		sys.stdout = sys.__stdout__

		ans = capture_output.getvalue().strip()
		self.assertTrue("DEPARTURE TRAIN_AB ENGINE ENGINE GHY GHY NJP NJP PTA NDL NDL AGA BPL NGP" in ans)


