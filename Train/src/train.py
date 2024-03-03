import conf
from collections import deque
from heapq import heappush, heappop


class Train:


	def __init__(self, name, train_path):
		self._train_path = train_path
		self.name = name
		self.train = deque()
		self.train_dist = []


	@property
	def train_path(self):
		return self._train_path

	@train_path.setter
	def train_path(self, new_train_path):
		self._train_path = new_train_path
	

	def ordered_boggey_by_distance(self, boggies):

		temp = []
		for boggey in boggies:
			if boggey in self.train_path:
				heappush(temp, (-self.train_path.get(boggey), boggey))
				heappush(self.train_dist, (self.train_path.get(boggey), boggey))

		while temp:
			dist, st = heappop(temp)
			self.train.append(st)


	def add_boggey(self, boggies):

		for boggey in boggies:
			boggey = boggey.strip()
			self.train.append(boggey)
			if conf.ENGINE != boggey:
				heappush(self.train_dist, (self.train_path.get(boggey, 0), boggey))

	def print_train(self, st=None):

		n = len(self.train)
		print(st, end=" ")
		print(self.name, end=" ")
		for index in range(n):
			print(self.train[index], end=" ")
			if index == n-1:
		 		print()

	def on_arrival(self, station):

		station_dist = self.train_path.get(station)
		while self.train_dist:
			dist, st = heappop(self.train_dist)
			if dist < self.train_path[station]:
				self.train.remove(st)
			else:
				heappush(self.train_dist, (dist, st))
				break
		self.print_train("ARRIVAL")










