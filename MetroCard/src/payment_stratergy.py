import conf
from src.enum import PersonType


class PaymentStratergy:

	SERVICE_COST = conf.SERVICE_COST
	RETURN_TRAVEL_DISCOUNT = conf.RETURN_TRAVEL_DISCOUNT

	def calculate_service_cost(self, amount):
		sevice_cost = int(amount * (self.SERVICE_COST/conf.HUNDRED_DIVISOR))
		return sevice_cost

	def calculate_return_travel_discount(self, amount):
		return int(amount * (self.RETURN_TRAVEL_DISCOUNT/conf.HUNDRED_DIVISOR))


	def return_travel_charge(self, metro_card, cost):

		discount = self.calculate_return_travel_discount(cost)
		pay_amount = cost - discount
		if metro_card.get_amount() < pay_amount:
			service_charge = self.calculate_service_cost(pay_amount-metro_card.get_amount())
			metro_card.update_amount(metro_card.get_amount())
			return pay_amount+service_charge, discount
		metro_card.update_amount(pay_amount)
		return pay_amount, discount

	def travel_charge(self, metro_card, cost):

		if metro_card.get_amount() < cost:
			service_charge = self.calculate_service_cost(cost-metro_card.get_amount())
			metro_card.update_amount(metro_card.get_amount())
			return cost+service_charge, 0
		metro_card.update_amount(cost)
		return cost, 0

	def pay(self, metro_card, person_type, is_return_travel):

		cost = conf.PERSON_TYPE_COST.get(person_type, 0)
		
		if is_return_travel:
			amount, discount = self.return_travel_charge(metro_card, cost)
			return amount, discount

		else:
			amount, discount = self.travel_charge(metro_card, cost)
			return amount, discount
