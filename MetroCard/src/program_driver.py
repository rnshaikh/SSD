import conf

from src.utils import format_params
from src.metrocard import MetroCard
from src.station import Station


class ProgramDriver:

	def __init__(self):
		self.stations = {}
		self.metro_cards = {}

	def add_metrocard(self, name, amount):
		metrocard = MetroCard(name, amount)
		self.metro_cards[name] = metrocard

	def add_station(self):
		self.stations[conf.STATION_1] = Station(conf.STATION_1)
		self.stations[conf.STATION_2] = Station(conf.STATION_2)

	def check_in(self, name, person_type, from_station):

		metrocard = self.metro_cards[name]
		amount, discount = metrocard.checked_in(person_type)
		self.stations[from_station].check_in(amount, discount, person_type)

	def print_summary(self):
		for station in self.stations:
			self.stations[station].print_summary()

	def parse_commands(self, file_path):

		with open(file_path, 'r') as fobj:
			for row in fobj:
				commands = row.split(" ")
				params = format_params(commands)
				if not params:
					getattr(self, conf.COMMANDS[params[conf.INIT_ZERO]['func']])()
				else:
					getattr(self, conf.COMMANDS[params[conf.INIT_ZERO]]['func'])(*params[conf.INIT_ONE:])


	
