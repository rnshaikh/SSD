import conf
from src.train import Train


class ProgramDriver:

	def __init__(self):

		self.trains = {}

	def add_train(self, name, boggies):

		train_obj = Train(name, conf.TRAIN_PATH[name])
		train_obj.add_boggey(boggies)
		self.trains[name] = train_obj

	def on_arrival(self):

		for train in self.trains:
			self.trains[train].on_arrival(conf.MERGE_STATION)

	def merge_train(self, trainA, trainB):
		train_obj = Train(conf.MERGE_TRAIN_NAME, conf.TRAIN_PATH[conf.MERGE_TRAIN_NAME])
		boggies = trainA.train + trainB.train
		train_obj.ordered_boggey_by_distance(boggies)
		return train_obj

	def on_deprature(self):

		train_obj = self.merge_train(*self.trains.values())
		train_obj.print_train(conf.DEPARTURE)


	def parse_commands(self, file_path):
		with open(file_path, 'r') as fobj:
			for row in fobj:
				boggies = row.split(" ")
				self.add_train(boggies[conf.INIT_ZERO], boggies[conf.INIT_ONE:])
				
		self.on_arrival()
		self.on_deprature()
