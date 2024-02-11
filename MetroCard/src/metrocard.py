from src.payment_stratergy import PaymentStratergy


class MetroCard:


	def __init__(self, name, amount):

		self.__name = name
		self.amount = amount
		self.check_in = None
		self.payment_stratergy = PaymentStratergy()

	def get_name(self):
		return self.__name 

	def get_amount(self):
		return self.amount

	def update_amount(self, amount):
		self.amount -= amount

	def update_travel_station(self):

		if self.is_return_travel():
			self.check_in = None
		else:
			self.check_in = True

	def is_return_travel(self):
		return self.check_in != None

	def checked_in(self, person_type):
		amount, discount = self.payment_stratergy.pay(self, person_type, self.is_return_travel())
		self.update_travel_station()
		return amount, discount

